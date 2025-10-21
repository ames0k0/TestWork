package main

import "fmt"

func sol(a int, b int) bool {
	if a == 10 || b == 10 { return true }
	if a + b == 10 { return true }
	return false
}

func test() {
	data	:= [5][2]int{{1, 10}, {10, 1}, {9,  1}, {8,  1}, {11, 1}}
	result	:= [5]bool{   true,    true,    true,    false,   false}
	for i := 0; i < len(data); i++ {
		a := data[i][0]
		b := data[i][1]
		r := result[i]
		v := sol(a, b)
		if v != r {
			fmt.Printf("sol(a=%v, b=%v) = (%v != %v)\n", a, b, v, r)
		}
	}
}

func main() { test() }
