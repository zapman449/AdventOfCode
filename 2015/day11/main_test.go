package main

import (
	"testing"
)

func TestIncrement(t *testing.T) {
	tests := []struct {
		name       string
		given      string
		want       string
	}{
		{
			"t1",
			"aa",
			"ab",
		},
		{
			"t2",
			"ah",
			"aj",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := increment(tt.given)
			if got != tt.want {
				t.Errorf("test %s failed - increment(%s) -> %s, wanted %s", tt.name, tt.given, got, tt.want)
			}
		})
	}
}

func TestRule3Q(t *testing.T) {
	tests := []struct {
		name       string
		given      string
		want       bool
	}{
		{
			"t1",
			"aaa",
			false,
		},
		{
			"t2",
			"aaaa",
			true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := rule3Q(tt.given)
			if got != tt.want {
				t.Errorf("test %s failed - increment(%s) -> %t, wanted %t", tt.name, tt.given, got, tt.want)
			}
		})
	}
}
