package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"

	"github.com/zapman449/adventOfCode/utilities"

	"github.com/alecthomas/kong"
)

type CLI struct {
	FileName string `arg:"" help:"filename to process"`
	Debug    bool   `arg:"debug" help:"Enable debug logging"`
}

// 20x3x11
// 15x27x5
// 6x29x7

var splitChar = "x"

func removeLargest(s []int64) []int64 {
    if len(s) == 0 {
        return s
    }
    maxVal := slices.Max(s)
    idx := slices.Index(s, maxVal)
    return slices.Delete(s, idx, idx+1)
}

func processLine(data string) (wrap int64, ribbon int64, err error) {
	vals := strings.Split(data, splitChar)
	l, errl := strconv.ParseInt(vals[0], 10, 64)
	w, errw := strconv.ParseInt(vals[1], 10, 64)
	h, errh := strconv.ParseInt(vals[2], 10, 64)
	if errl != nil || errw != nil || errh != nil {
		return 0, 0, fmt.Errorf("err failed to parse to int - line %s - %v - %v - %v", data, errl, errw, errh)
	}
	sides := []int64{l*w, l*h, w*h}

	minSide := slices.Min(sides)
	wrap = 2*l*w + 2*l*h + 2*w*h + minSide

	ribbonSides := []int64{l, w, h}

	vol := l*w*h
	twoSmallSides := removeLargest(ribbonSides)
	ribbon = 2*twoSmallSides[0] + 2*twoSmallSides[1] + vol
	// fmt.Printf("%d %d %d -> %v %d %d %d -> %d\n",l,w,h, twoSmallSides, 2*twoSmallSides[0], 2*twoSmallSides[1], vol, ribbon)
	
	return wrap, ribbon, err
}

func main() {
	// todo: import kong, read filename from input
	var cli CLI
	_ = kong.Parse(&cli)
	var p1Tally int64
	var p2Tally int64
	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines failed: %v", err)
			os.Exit(1)
		}
		wrap, ribbon, err := processLine(line)
		if err != nil {
			fmt.Printf("processLine failed for line %s: %v", line, err)
			os.Exit(1)
		}
		p1Tally += wrap
		p2Tally += ribbon
	}
	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
