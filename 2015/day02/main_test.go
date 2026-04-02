package main

import "testing"

func TestProcessFloors(t *testing.T) {
	tests := []struct {
		name    string
		given   string
		wantW   int64
		wantR   int64
		wantErr bool
	}{
		{
			"t1",
			"2x3x4",
			58,
			34,
			false,
		},
		{
			"t2",
			"1x1x10",
			43,
			14,
			false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotW, gotR, err := processLine(tt.given)
			if err != nil && tt.wantErr {
				// no-op
			} else if err == nil && !tt.wantErr {
				// no-op
			} else {
				t.Errorf("test %s failed - processLine(%s) -> error %v but wantErr is %t", tt.name, tt.given, err, tt.wantErr)
			}
			if gotW != tt.wantW {
				t.Errorf("test %s failed - processLine(%s) -> %d, %d, wanted %d, %d", tt.name, tt.given, gotW, gotR, tt.wantW, tt.wantR)
			}
		})
	}
}
