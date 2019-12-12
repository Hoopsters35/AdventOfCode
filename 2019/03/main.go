package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func ManhattanDistance(x1, y1, x2, y2 int) int {
	d1 := x1 - x2
	if d1 < 0 {
		d1 = -d1
	}
	d2 := y1 - y2
	if d2 < 0 {
		d2 = -d2
	}
	return d1 + d2
}

func GetInput() []string {
	bytes, _ := ioutil.ReadFile("data.txt")
	paths := strings.Split(string(bytes), "\n")

	return paths[0:2]
}

func ProcessPath(input string) []string {
	var path []string
	for _, s := range strings.Split(input, ",") {
		path = append(path, s)
	}

	return path
}

func RunPath(grid [][]string, []string path) [][]string {
	i, j := 0
	for _, s := range path {
		switch s[0] {
		case 'L':
			count := 1
			for count <=  strconv.Atoi(s[1:]) {
				grid[i - count]
			}
		}
	}
}

func main() {
	// input := GetInput()

	// path1 := ProcessPath(input[0])
	// path2 := ProcessPath(input[1])

	test11 := ProcessPath("R8,U5,L5,D3")
	test12 := ProcessPath("U7,R6,D4,L4")

	fmt.Println(test11)
	fmt.Println(test12)

	// var grid [1500][1500]int
}
