package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"

	"github.com/zapman449/adventOfCode/utilities"

	"github.com/alecthomas/kong"
)

type CLI struct {
	FileName string `arg:"" help:"filename to process"`
	Debug    bool   `arg:"debug" default:"false" help:"Enable debug logging"`
}

type Question struct {
	LeftSymbol  string
	FoundLeft   bool
	LeftInt     uint16
	RightSymbol string
	FoundRight  bool
	RightInt    uint16
	Operator    string
	Original    string
	Value       uint16
}

func (q *Question) GotLeft() bool {
	if q.Operator == "NOT" || q.Operator == "CLONE" {
		return true
	}
	return q.FoundLeft
}

func (q *Question) GotRight() bool {
	return q.FoundRight
}

func (q *Question) SetLeft(i uint16) {
	q.LeftInt = i
	q.FoundLeft = true
}

func (q *Question) SetRight(i uint16) {
	q.RightInt = i
	q.FoundRight = true
}

func (q *Question) Do() (value uint16) {
	switch q.Operator {
	case "AND": value = q.LeftInt & q.RightInt
	case "OR": value = q.LeftInt | q.RightInt
	case "LSHIFT": value = q.LeftInt << q.RightInt
	case "RSHIFT": value = q.LeftInt >> q.RightInt
	case "NOT": value = ^q.RightInt
	case "CLONE": value = q.RightInt // handle ww -> qq pattern
	}
	q.Value = value
	return value
}

func processLine(line string, debug bool) (isQuestion bool, question *Question, wire string, answer uint16) {
	words := strings.Split(line, " ")

	// ## -> wire
	m1a, _ := regexp.Match(`^[0-9]+ -> [a-z]+$`, []byte(line))
	m1b, _ := regexp.Match(`^[a-z]+ -> [a-z]+$`, []byte(line))
	if m1a { // handle value to wire 
		i, _ := strconv.ParseUint(words[0], 10, 16)
		return isQuestion, question, words[2], uint16(i)
	} else if m1b {
		// wire to wire copy
		isQuestion = true
		q := Question{"", false, 0, words[0], false, 0, "CLONE", line, 0}
		return isQuestion, &q, words[2], 0
	}

	// NOT <wire|#> -> wire
	if words[0] == "NOT" { // handle odd NOT case
		wire := words[3]
		m2, _ := regexp.Match(`^[a-z]+$`, []byte(words[1]))
		if m2 {
			isQuestion = true
			q := Question{"", false, 0, words[1], false, 0, "NOT", line, 0}
			question = &q
			if debug {
				fmt.Printf("DEBUG-a: %s -> %t, --%+v--, %s, %d\n", line, isQuestion, question, wire, answer)
			}
			return isQuestion, question, wire, answer
		} else {
			i, _ := strconv.ParseUint(words[1], 10, 16)
			if debug {
				fmt.Printf("DEBUG-b: %s -> %t, --%+v--, %s, %d\n", line, isQuestion, question, wire, answer)
			}
			return isQuestion, question, words[3], ^uint16(i)
		}
	}

	// <w|#> <AND|OR|LSHIFT|RSHIFT> <w|n> -> wire
	wire = words[4]
	operator := words[1]
	m3a, _ := regexp.Match(`^[a-z]+$`, []byte(words[0]))
	m3b, _ := regexp.Match(`^[a-z]+$`, []byte(words[2]))
	var q Question
	if !m3a && !m3b {
		// two numbers, answer it
		i, _ := strconv.ParseUint(words[0], 10, 16)
		j, _ := strconv.ParseUint(words[2], 10, 16)
		q = Question{"", true, uint16(i), "", true, uint16(j), operator, line, 0}
		answer = q.Do()
		return isQuestion, question, wire, answer
	} else if !m3a {
		// first is number
		isQuestion = true
		i, _ := strconv.ParseUint(words[0], 10, 16)
		q = Question{"", true, uint16(i), words[2], false, 0, operator, line, 0}
	} else if !m3b {
		// second is number
		isQuestion = true
		j, _ := strconv.ParseUint(words[2], 10, 16)
		q = Question{words[0], false, 0, "", true, uint16(j), operator, line, 0}
	} else {
		// both wires
		isQuestion = true
		q = Question{words[0], false, 0, words[2], false, 0, operator, line, 0}
	}
	return isQuestion, &q, wire, answer
}

func recurse(questions map[string]*Question, answers map[string]uint16, wire string) uint16 {
	a, ok := answers[wire]
	if ok {
		return a
	}
	q := questions[wire]

	if !q.GotLeft() {
		a, ok = answers[q.LeftSymbol]
		if ok {
			q.SetLeft(a)
		} else {
			v := recurse(questions, answers, q.LeftSymbol)
			q.SetLeft(v)
			answers[q.LeftSymbol] = v
		}
	}
	if !q.GotRight() {
		a, ok = answers[q.RightSymbol]
		if ok {
			q.SetRight(a)
		} else {
			v := recurse(questions, answers, q.RightSymbol)
			q.SetRight(v)
			answers[q.RightSymbol] = v
		}
	}
	v := q.Do()
	answers[wire] = v
	return v
}

var EndWire = "a"

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	var p1Tally int64
	var p2Tally int64

	// part1
	questions := make(map[string]*Question)
	answers := make(map[string]uint16)
	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines() failed: %v", err)
			os.Exit(1)
		}
		isQ, question, wire, answer := processLine(line, cli.Debug)
		if isQ {
			questions[wire] = question
		} else {
			answers[wire] = answer
		}
	}
	p1 := recurse(questions, answers, EndWire)
	p1Tally = int64(p1)

	// part2: take the new value for a from p1, set that as value for b, otherwise re-run from beginning.
	questions = make(map[string]*Question)
	answers = make(map[string]uint16)
	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines() failed: %v", err)
			os.Exit(1)
		}
		isQ, question, wire, answer := processLine(line, cli.Debug)
		if isQ {
			questions[wire] = question
		} else {
			answers[wire] = answer
		}
	}
	answers["b"] = p1
	p2 := recurse(questions, answers, EndWire)
	p2Tally = int64(p2)

	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
