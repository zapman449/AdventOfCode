package utilities

import (
	"bufio"
	"fmt"
	"iter"
	"os"
)

func GenerateLines(fileName string) iter.Seq2[string, error] {
    return func(yield func(string, error) bool) {
        file, err := os.Open(fileName)
        if err != nil {
            yield("", fmt.Errorf("filed to open file %s - err: %v", fileName, err))
            return
        }
        defer file.Close()

        scanner := bufio.NewScanner(file)
        for scanner.Scan() {
            if !yield(scanner.Text(), nil) {
                return
            }
        }
    }
}
