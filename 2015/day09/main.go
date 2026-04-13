package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/zapman449/adventOfCode/utilities"

	"github.com/alecthomas/kong"
)

type CLI struct {
	FileName string `arg:"" help:"filename to process"`
	Debug    bool   `arg:"debug" default:"false" help:"Enable debug logging"`
}

func processLine(
	line string,
	cities map[string]bool,
	distances map[string]map[string]int64, debug bool) {

	// X to Y = ###
	words := strings.Split(line, " ")
	start := words[0]
	end := words[2]
	d := words[4]
	dist, _ := strconv.ParseInt(d, 10, 64)
	cities[start] = true
	cities[end] = true
	_, ok := distances[start]
	if !ok {
		distances[start] = make(map[string]int64)
	}
	_, ok = distances[end]
	if !ok {
		distances[end] = make(map[string]int64)
	}
	distances[start][end] = dist
	distances[end][start] = dist
	return
}

func tally(cityList []string, distances map[string]map[string]int64, debug bool) (t int64) {
	pc := ""
	for _, c := range cityList {
		if pc != "" {
			t += distances[pc][c]
		}
		pc = c
	}
	return t
}

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	var p1Tally int64
	var p2Tally int64

	cities := make(map[string]bool)
	distances := make(map[string]map[string]int64)

	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines() failed: %v", err)
			os.Exit(1)
		}
		processLine(line, cities, distances, cli.Debug)
	}
	var cityList []string
	for k := range cities {
		cityList = append(cityList, k)
	}
	for perm := range utilities.Permutations(cityList) {
		t := tally(perm, distances, cli.Debug)
		if p1Tally == 0 {
			p1Tally = t
		} else if t < p1Tally {
			p1Tally = t
		}
		if p2Tally == 0 {
			p2Tally = t
		} else if t > p2Tally {
			p2Tally = t
		}
	}

	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
