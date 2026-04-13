package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/alecthomas/kong"
)

type CLI struct {
	// FileName string `arg:"" help:"filename to process"`
	Debug    bool   `arg:"debug" default:"false" help:"Enable debug logging"`
}

// var given = "1"
// var iterations = 5

var given = "1321131112"

func lookAndSay(given string, iterations int, debug bool) (result int64) {
	for i := range iterations {
		var newgiven strings.Builder
		var pc string
		var c string
		var counter int
		for _, cr := range given {
			c = string(cr)
			if pc == "" {
				counter += 1
			} else if pc == c {
				counter += 1
			} else {
				// newgiven = fmt.Sprintf("%s%d%s", newgiven, counter, pc)
				newgiven.WriteString(strconv.Itoa(counter))
				newgiven.WriteString(pc)
				counter = 1
			}
			_ = i - 1
			// if debug { fmt.Printf("iter %d, given %s, pc %s, c %s, newgiven %s\n", i, given, pc, c, newgiven.String())}
			pc = c
		}
		// newgiven = fmt.Sprintf("%s%d%s", newgiven, counter, pc)
		newgiven.WriteString(strconv.Itoa(counter))
		newgiven.WriteString(pc)
		given = newgiven.String()
	}
	result = int64(len(given))
	if debug { fmt.Printf("over %d iterations yields len(newgiven) %d, newgiven: %s\n", iterations, result, given)}
	return result
}

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	var p0Tally int64
	var p1Tally int64
	var p2Tally int64

	p0Tally = lookAndSay("1", 5, cli.Debug)
	p1Tally = lookAndSay(given, 40, cli.Debug)
	p2Tally = lookAndSay(given, 50, cli.Debug)

	fmt.Printf("p0 result: %d\n", p0Tally)
	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
