package main

import "testing"

func TestProcessFloors(t *testing.T) {
	tests := []struct {
		name    string
		given   string
		wantF   int64
		wantB   int64
		wantErr bool
	}{
		{
			"nested_zero",
			"(())",
			0,
			0,
			false,
		},
		{
			"sequential_zero",
			"()()",
			0,
			0,
			false,
		},
		{
			"basement1",
			")",
			-1,
			1,
			false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotF, gotB, err := processFloors(tt.given)
			if err != nil && tt.wantErr {
				// no-op
			} else if err == nil && !tt.wantErr {
				// no-op
			} else {
				t.Errorf("test %s failed - processFloors(%s) -> error %v but wantErr is %t", tt.name, tt.given, err, tt.wantErr)
			}
			if gotF != tt.wantF {
				t.Errorf("test %s failed floor - processFloors(%s) -> %d, wanted %d", tt.name, tt.given, gotF, tt.wantF)
			} else if gotB != tt.wantB {
				t.Errorf("test %s failed basement - processFloors(%s) -> %d, wanted %d", tt.name, tt.given, gotB, tt.wantB)
			}
		})
	}
}
