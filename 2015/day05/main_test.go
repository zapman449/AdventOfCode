package main

import "testing"

func TestIsNiceQ(t *testing.T) {
	tests := []struct {
		name    string
		given   string
		want   bool
	}{
		{
			"t1",
			"aeiouaeiouaeiou",
			false,
		},
		{
			"t2",
			"aabbccdd",
			false,
		},
		{
			"t3",
			"aabbccdd",
			false,
		},
		{
			"t_works",
			"aeiff",
			true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, _ := isNiceQ(tt.given, true)
			if got != tt.want {
				t.Errorf("test %s failed - isNiceQ(%s) -> %t, wanted %t", tt.name, tt.given, got, tt.want)
			}
		})
	}
}

func TestIsNiceQ2(t *testing.T) {
	tests := []struct {
		name    string
		given   string
		want   bool
	}{
		{
			"2-t1",
			"qjhvhtzxzqqjkmpb",
			true,
		},
		{
			"2-t2",
			"xxyxx",
			true,
		},
		{
			"2-t3",
			"aaa",
			false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, _ := isNiceQ2(tt.given, true)
			if got != tt.want {
				t.Errorf("test %s failed - isNiceQ2(%s) -> %t, wanted %t", tt.name, tt.given, got, tt.want)
			}
		})
	}
}
