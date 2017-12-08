package main

import (
	"io/ioutil"
	"fmt"
	"strconv"
)

func main() {
	b,_ := ioutil.ReadFile("input.txt")
	capcha := string(b)
	fmt.Println(capcha)
	first,_ := strconv.Atoi(string(capcha[0]))
	last := -1

	sum := 0
	previous := -1
	for _, rune := range capcha {
		curr,_ := strconv.Atoi(string(rune))
		last = curr
		if curr == previous {
			sum += curr
		}
		previous = curr
	}
	if first == last {
		sum += first
	}
	fmt.Println(sum)
	
}