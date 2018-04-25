package main

import "fmt"

func main() {
	fmt.Println("NL SANDEEP")
	var a1 [5]int
	a2 := [...]int{1, 2, 3, 4, 5}

	for i := 0; i < 5; i++ {
		fmt.Print(" ", a1[i])
		fmt.Print(a2[i])
	}


}
