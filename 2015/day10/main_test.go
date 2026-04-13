package main

import (
	"testing"
)

func TestQuestionDo(t *testing.T) {
	tests := []struct {
		name       string
		given      string
		iterations int
		want       int64
		debug      bool
	}{
		{
			"t1",
			"1",
			5,
			6,
			true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := lookAndSay(tt.given, tt.iterations, tt.debug)
			if got != tt.want {
				t.Errorf("test %s failed - speakAndSay(%s, %d) -> %d, wanted %d", tt.name, tt.given, tt.iterations, got, tt.want)
			}
		})
	}
}
