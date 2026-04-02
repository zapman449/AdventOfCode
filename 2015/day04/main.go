package main

import (
	"crypto/md5"
	"fmt"
	// "runtime"
	// "os"
	"strconv"
	"sync"
	"sync/atomic"
)

var given = []byte("bgvyzdsv")

func testint(given []byte, i int64, debug bool) (got5, got6 bool) {
	buf := make([]byte, 0, 32)
	buf = strconv.AppendInt(buf[:len(given)], i, 10)
	copy(buf, given)
	h := md5.Sum(buf)
	if h[0] == 0 && h[1] == 0 && h[2] < 0x10 { // 5 hex zeros
		got5 = true
		if h[2] == 0 { // 6 hex zeros
			got6 = true
		}
	}
	if debug {
		fmt.Printf("%s %d -> %s %s -> %t %t\n", string(given), i, string(buf), string(h[:]), got5, got6)
	}
	return got5, got6
}

// Normally the atomic types shouldn't be used, better to use the higher level channels / other sync module
// tooling, but in this case, the channels overhead outweighs the loop cost.
// This approach takes 0.03s
// the iterative approach takes 0.13s
// the channels approach was taking 0.5s, but there was optimizations to be found. I suspect it could get 
// down to where iterative was however.
func testRange(start, stride int64, five, six *atomic.Int64, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := start; i < 10_000_000; i += stride {
		// Stop early once both are found
		if five.Load() > 0 && six.Load() > 0 {
			return
		}
		got5, got6 := testint(given, i, false)
		if got5 {
			five.CompareAndSwap(0, i)
			if got6 {
				six.CompareAndSwap(0, i)
			}
		}
	}
}

func main() {
	// // iterative way
	// for i:=int64(1); i<10000000; i++ {
	// 	isfive, issix := testint(given, i, false)
	// 	if isfive {
	// 		fmt.Printf("5zeros: %d\n", i)
	// 	}
	// 	if issix {
	// 		fmt.Printf("6zeros: %d\n", i)
	// 		os.Exit(0)
	// 	}
	// }
	// os.Exit(1)

	// workers := int64(runtime.NumCPU())
	workers := int64(8)
	var five, six atomic.Int64
	var wg sync.WaitGroup
	for w := int64(1); w <= workers; w++ {
		wg.Add(1)
		go testRange(w, workers, &five, &six, &wg)
	}
	wg.Wait()
	fmt.Printf("p1 result: %d\n", five.Load())
	fmt.Printf("p2 result: %d\n", six.Load())
}
