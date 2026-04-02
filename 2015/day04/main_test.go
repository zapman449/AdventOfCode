package main

import "testing"

func TestTestint(t *testing.T) {
	tests := []struct {
		name    string
		given   []byte
		i       int64
		want5   bool
		want6   bool
	}{
		{
			"t1",
			[]byte("abcdef"),
			609043,
			true,
			false,
		},
		{
			"t2",
			[]byte("pqrstuv"),
			1048970,
			true,
			false,
		},
		{
			"t3",
			[]byte("pqrstuv"),
			1048971,
			false,
			false,
		},
		{
			"t4",
			[]byte("bgvyzdsv"),
			1038736,
			true,
			true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got5, got6 := testint(tt.given, tt.i, true)
			if got5 != tt.want5 || got6 != tt.want6 {
				t.Errorf("test %s failed - testint(%x, %d) -> %t, %t, wanted %t, %t", tt.name, tt.given, tt.i, got5, got6, tt.want5, tt.want6)
			}
		})
	}
}
