package main

import (
	"fmt"
	"os"
	"regexp"
	"strings"

	"github.com/zapman449/adventOfCode/utilities"

	"github.com/alecthomas/kong"
)

type CLI struct {
	FileName string `arg:"" help:"filename to process"`
	//Debug    bool   `arg:"debug" help:"Enable debug logging"`
}

func isNiceQ(line string, debug bool) (bool, error) {
	t1, t2, t3 := false, false, false
	var cp string
	vowels := "aeiou"
	vcount := 0
	for _, cr := range line {
		c := string(cr)
		if strings.Contains(vowels, c) {
			vcount += 1
		}
		if c == cp {
			t2 = true
		}
		cp = c
	}
	if vcount >= 3 {
		t1 = true
	}

	matched, err := regexp.Match(`(ab|cd|pq|xy)`, []byte(line))
	if err != nil {
		return false, fmt.Errorf("regex match failed - err: %v", err)
	}
	if !matched {
		t3 = true
	}
	if debug {
		fmt.Printf("%s - %d %t - %t - %t\n", line, vcount, t1, t2, t3)
	}
	return t1 && t2 && t3, nil
}

func isNiceQ2(line string, debug bool) (bool, error) {
	t1, t2 := false, false
	var cp string
	var cpp string
	for i, cr := range line {
		c := string(cr)
		if i < len(line)-1 && cp != "" {
			if strings.Contains(line[i+1:], fmt.Sprintf("%s%s", cp, c)) {
				t1 = true
			}
		}
		if cpp != "" && cpp == c {
			t2 = true
		}
		cpp = cp
		cp = c
	}
	if debug {
		fmt.Printf("%s - %t - %t\n", line, t1, t2)
	}
	return t1 && t2, nil
}

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	var p1Tally int64
	var p2Tally int64
	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines failed: %v", err)
			os.Exit(1)
		}

		isNice, err := isNiceQ(line, false)
		if err != nil {
			fmt.Printf("isNiceQ failed for line %s - err: %v\n", line, err)
		}
		if isNice {
			p1Tally += 1
		}

		isNice2, err := isNiceQ2(line, false)
		if err != nil {
			fmt.Printf("isNiceQ2 failed for line %s - err: %v\n", line, err)
		}
		if isNice2 {
			p2Tally += 1
		}
	}
	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
