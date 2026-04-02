package main

import (
	"fmt"
	"os"
)

func processFloors(data string) (floors int64, basementPos int64, err error) {
	for i, c := range data {
		c_str := string(c)
		if c_str == "(" {
			floors += 1
		} else if c_str == ")" {
			floors -= 1
			if basementPos == 0 && floors == -1 {
				basementPos = int64(i+1)
			}
		} else if c_str == "\n" {
			break
		} else {
			return 0, 0, fmt.Errorf("error: unknown char %s at idx %d", c_str, i)
		}
	}
	return floors, basementPos, err
}

func main() {
	data_bytes, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Printf("error reading input.txt: %v\n", err)
		os.Exit(1)
	}
	data := string(data_bytes)
	floors, basementPos, err := processFloors(data)
	if err != nil {
		fmt.Printf("error: failed to processFloors: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("p1 result: %d\n", floors)
	fmt.Printf("p2 result: %d\n", basementPos)
}
