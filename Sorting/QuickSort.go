package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	slice := genSlice(20)
	fmt.Println("\n\n -- Unsorted ---\n", slice)
	quickSort(slice)
	fmt.Println("\n\n -- Sorted ---\n", slice)
}

func genSlice(size int) []int {
	slice := make([]int, size, size)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size; i++ {
		slice[i] = rand.Intn(900) - rand.Intn(900)
	}
	return slice
}

func quickSort(a []int) []int {
	if len(a) < 2 {
		return a
	}
	left, right := 0, len(a)-1
	pivot := rand.Int() % len(a)
	a[pivot], a[right] = a[right], a[pivot]

	for i, _ := range a {
		if a[i] < a[right] {
			a[left], a[i] = a[i], a[left]
			left++
		}
	}
	a[left], a[right] = a[right], a[left]
	quickSort(a[:left])
	quickSort(a[left+1:])
	return a

}
