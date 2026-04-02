package main

import (
	"fmt"
	"os"

	"github.com/zapman449/adventOfCode/utilities"

	"github.com/alecthomas/kong"
)

type CLI struct {
	FileName string `arg:"" help:"filename to process"`
	//Debug    bool   `arg:"debug" help:"Enable debug logging"`
}

type pointInfo struct {
	Visited    bool
	VisitCount int64
}
func (p pointInfo) visit() {
	p.Visited = true
	p.VisitCount = p.VisitCount + 1
}

func processLine(line string) (visited int64, visited2 int64, err error) {
	p := utilities.NewPoint(0, 0)
	pointMap := make(map[utilities.Point]pointInfo)
	var pi0 pointInfo
	pi0.visit()
	pointMap[p] = pi0

	pointMap2 := make(map[utilities.Point]pointInfo)
	var pi0a pointInfo
	pi0a.visit()
	pointMap[p] = pi0a
	pS := utilities.NewPoint(0,0)
	pR := utilities.NewPoint(0,0)
	moveSanta := true

	for _, cr := range line {
		c := string(cr)
		var np utilities.Point
		var npS utilities.Point
		var npR utilities.Point
		var pi pointInfo
		if c == "^" {
			np = p.Up()
			if moveSanta {
				npS = pS.Up()
			} else {
				npR = pR.Up()
			}
		} else if c == "v" {
			np = p.Down()
			if moveSanta {
				npS = pS.Down()
			} else {
				npR = pR.Down()
			}
		} else if c == ">" {
			np = p.Right()
			if moveSanta {
				npS = pS.Right()
			} else {
				npR = pR.Right()
			}
		} else if c == "<" {
			np = p.Left()
			if moveSanta {
				npS = pS.Left()
			} else {
				npR = pR.Left()
			}
		} else {
			return visited, visited2, fmt.Errorf("invalid char --%s--\n", c)
		}
		pi, ok := pointMap[np]
		if !ok {
			pi = pointInfo{true, 0}
		}
		pi.visit()
		pointMap[np] = pi
		p = np

		if moveSanta {
			pi, ok = pointMap2[npS]
		} else {
			pi, ok = pointMap2[npR]
		}
		if !ok {
			pi = pointInfo{true, 0}
		}
		pi.visit()
		if moveSanta {
			pointMap2[npS] = pi
			pS = npS
		} else {
			pointMap2[npR] = pi
			pR = npR
		}
		moveSanta = !moveSanta
	}
	visited = int64(len(pointMap))
	visited2 = int64(len(pointMap2))
	return visited, visited2, err
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
		p1Tally, p2Tally, err = processLine(line)
		break
	}
	fmt.Printf("p1 result: %d\n", p1Tally)
	fmt.Printf("p2 result: %d\n", p2Tally)
}
