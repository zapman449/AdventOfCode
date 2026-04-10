package main

import (
	"testing"
)

func TestQuestionDo(t *testing.T) {
	tests := []struct {
		name     string
		question Question
		wantV    uint16
	}{
		{
			"t1 AND",
			Question{"", true, 123, "", true, 456, "AND", "x AND y -> d", 0},
			72,
		},
		{
			"t2 OR",
			Question{"", true, 123, "", true, 456, "OR", "x OR y -> e", 0},
			507,
		},
		{
			"t3 LSHIFT",
			Question{"", true, 123, "", true, 2, "LSHIFT", "x LSHIFT 2 -> f", 0},
			492,
		},
		{
			"t4 RSHIFT",
			Question{"", true, 456, "", true, 2, "RSHIFT", "y RSHIFT 2 -> g", 0},
			114,
		},
		{
			"t5 NOT",
			Question{"", true, 0, "", true, 123, "NOT", "NOT x -> h", 0},
			65412,
		},
		{
			"t6 NOT",
			Question{"", true, 0, "", true, 456, "NOT", "NOT y -> i", 0},
			65079,
		},
		{
			"t7 canNotDo1",
			Question{"", true, 0, "", true, 456, "AND", "x AND y -> i", 0},
			0,
		},
		{
			"t8 canNotDo2",
			Question{"", true, 123, "", true, 0, "AND", "x AND y -> i", 0},
			0,
		},
		{
			"t9 canNotDo3",
			Question{"", true, 0, "", true, 0, "NOT", "NOT y -> i", 0},
			65535,
		},
		{
			"t10 CLONE",
			Question{"", true, 0, "", true, 3, "CLONE", "y -> i", 0},
			3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotValue := tt.question.Do()
			if gotValue != tt.wantV {
				t.Errorf("test %s failed - question.Do() value -> %d, wanted %d", tt.name, gotValue, tt.wantV)
			}
		})
	}
}
