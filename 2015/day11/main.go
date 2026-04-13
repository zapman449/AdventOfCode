package main

import (
	"fmt"
	"strings"

	"github.com/alecthomas/kong"
)

type CLI struct {
	// FileName string `arg:"" help:"filename to process"`
	Debug    bool   `name:"debug" default:"false" help:"Enable debug logging"`
}

var given = "cqjxjnds"

var nextLetter = map[string]string{
	"a": "b",
	"b": "c",
	"c": "d",
	"d": "e",
	"e": "f",
	"f": "g",
	"g": "h",
	"h": "j",
	"j": "k",
	"k": "m",
	"m": "n",
	"n": "p",
	"p": "q",
	"q": "r",
	"r": "s",
	"s": "t",
	"t": "u",
	"u": "v",
	"v": "w",
	"w": "x",
	"x": "y",
	"y": "z",
	// Omit z so map lookup fails
}

var straights = []string{
	// omit straights with i, l, or o
	"abc",
	"bcd",
	"cde",
	"def",
	"efg",
	"fgh",
	"pqr",
	"qrs",
	"rst",
	"stu",
	"tuv",
	"uvw",
	"vwx",
	"wxy",
	"xyz",
}

func rule1Q(input string) bool {
	for _, s := range straights {
		if strings.Contains(input, s) {
			return true
		}
	}
	return false
}

func rule2Q(input string) bool {
	for _, s := range []string{"i", "l", "o"} {
		if strings.Contains(input, s) {
			return false
		}
	}
	return true
}

func rule3Q(input string) bool {
	var pc string
	var pairs int
	for i := range len(input) {
		c := string(input[i])
		if pc == "" {
			pc = c
			continue
		}

		if pc == c {
			if pairs == 0 {
				pairs += 1
			} else {
				return true
			}
			pc = ""  // clear pc so "aaa" doesn't count as two pairs
		} else {
			pc = c
		}
	}
	return false
}

func increment(input string) string {
	intermediate := strings.Split(input, "")
	for i := len(input)-1; i>=0; i-- {
		if intermediate[i] == "z" {
			intermediate[i] = "a"
		} else {
			c := nextLetter[intermediate[i]]
			intermediate[i] = c
			break
		}
	}
	return strings.Join(intermediate, "")
}

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	var p1Tally string
	var p2Tally string

	g := given
	for {
		g = increment(g)
		q1 := rule1Q(g)
		q2 := rule2Q(g)
		q3 := rule3Q(g)
		if q1 && q2 && q3 {
			if p1Tally == "" {
				p1Tally = g
			} else if p2Tally == "" {
				p2Tally = g
				break
			}
		}
		if cli.Debug {
			fmt.Printf("g is %s, %t %t %t\n", g, q1, q2, q3)
		}
	}

	fmt.Printf("p1 result: %s\n", p1Tally)
	fmt.Printf("p2 result: %s\n", p2Tally)
}
