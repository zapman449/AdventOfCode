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

type Light struct {
	On         bool
	Brightness int64
}

func (l *Light) Toggle() {
	l.On = !l.On
	l.Brightness += 2
}

func (l *Light) TurnOn() {
	l.On = true
	l.Brightness += 1
}

func (l *Light) TurnOff() {
	l.On = false
	if l.Brightness <= 1 {
		l.Brightness = 0
	} else {
		l.Brightness -= 1
	}
}

// var Data map[utilities.Point]*Light

func processLine(line string, data map[utilities.Point]*Light, debug bool) error {
	if strings.HasPrefix(line, "turn o") {
		// allign columns. 'turn on' and 'turn off' become 'turn_on' and 'turn_off' to match "toggle"
		line = line[:4] + "_" + line[5:]
	}
	words := strings.Split(line, " ")
	onOffToggleStr := words[0]
	startCorner := words[1]
	endCorner := words[3]
	words = strings.Split(startCorner, ",")
	startX, errX := strconv.ParseInt(words[0], 10, 64)
	startY, errY := strconv.ParseInt(words[1], 10, 64)
	if errX != nil || errY != nil {
		return fmt.Errorf("failed to parse startX,startY from line %s", line)
	}
	words = strings.Split(endCorner, ",")
	endX, errX := strconv.ParseInt(words[0], 10, 64)
	endY, errY := strconv.ParseInt(words[1], 10, 64)
	if errX != nil || errY != nil {
		return fmt.Errorf("failed to parse startX,startY from line %s", line)
	}
	var counter int64
	for x := startX; x <= endX; x++ {
		for y := startY; y <= endY; y++ {
			p := utilities.NewPoint(x, y)
			lp, ok := data[p]
			if !ok {
				l := Light{false, 0}
				lp = &l
			}
			switch onOffToggleStr {
			case "turn_on":  lp.TurnOn()
			case "turn_off": lp.TurnOff()
			case "toggle":   lp.Toggle()
			}
			data[p] = lp
			counter += 1
		}
	}
	if debug {
		fmt.Printf("for line %s twiddled %d lights", line, counter)
	}
	return nil
}

func processData(data map[utilities.Point]*Light) (p1Tally, p2Tally int64) {
	for _, light := range data {
		if light.On {
			p1Tally += 1
		}
		p2Tally += light.Brightness
	}
	return p1Tally, p2Tally
}

func main() {
	var cli CLI
	_ = kong.Parse(&cli)
	data := make(map[utilities.Point]*Light)
	var p1Tally int64
	var p2Tally int64
	for line, err := range utilities.GenerateLines(cli.FileName) {
		if err != nil {
			fmt.Printf("GenerateLines() failed: %v", err)
			os.Exit(1)
		}
		err = processLine(line, data, cli.Debug)
		if err != nil {
			fmt.Printf("processLine() failed: %v", err)
			os.Exit(1)
		}
	}
	p1Tally, p2Tally = processData(data)
	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
