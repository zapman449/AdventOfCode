package main

import (
	"fmt"
	"os"
	"strconv"

	"github.com/zapman449/adventOfCode/utilities"

	"github.com/alecthomas/kong"
)

type CLI struct {
	FileName string `arg:"" help:"filename to process"`
	Debug    bool   `arg:"debug" default:"false" help:"Enable debug logging"`
}

func unquote(str string) string {
	s, _ := strconv.Unquote(str)
	return s
}

func quote(str string) string {
	s := strconv.Quote(str)
	return s
}

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	var p1Tally int64
	var p2Tally int64

	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines() failed: %v", err)
			os.Exit(1)
		}
		p1Tally += int64(len(line)) - int64(len(unquote(line)))
		p2Tally += int64(len(quote(line))) - int64(len(line))
	}

	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
