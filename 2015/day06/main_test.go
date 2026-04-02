package main

import (
	"testing"
	
	"github.com/zapman449/adventOfCode/utilities"
)

func TestProcessData(t *testing.T) {
	tests := []struct {
		name    string
		lines   []string
		wantP1  int64
		wantP2  int64
	}{
		{
			"t1 turn_on",
			[]string{"turn on 0,0 through 0,5",},
			6,
			6,
		},
		{
			"t2 turn_off",
			[]string{"turn on 0,0 through 0,5", "turn off 0,0 through 0,2"},
			3,
			3,
		},
		{
			"t3 toggle",
			[]string{"turn on 0,0 through 0,5", "toggle 0,3 through 0,8"},
			6,
			18,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			data := make(map[utilities.Point]*Light)
			for _, line := range tt.lines {
				_ = processLine(line, data, true)
			}
			gotP1, gotP2 := processData(data)
			if gotP1 != tt.wantP1 {
				t.Errorf("test %s failed P1 - processData() -> %d, wanted %d", tt.name, gotP1, tt.wantP1)
			}
			if gotP2 != tt.wantP2 {
				t.Errorf("test %s failed P2 - processData() -> %d, wanted %d", tt.name, gotP2, tt.wantP2)
			}
		})
	}
}
