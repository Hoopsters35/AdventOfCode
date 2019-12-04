package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func fuelRequired(mass int) int {
	fuel := mass / 3
	fuel = int(fuel)
	return fuel - 2
}

func main() {
	/*
	 * Test givens
	 */
	test := [4]int{12, 14, 1969, 100756}
	testAns := [4]int{2, 2, 654, 33583}

	for i := 0; i < len(test); i++ {
		val := fuelRequired(test[i])
		fmt.Printf("%d returned %d: %t\n", test[i], val, val == testAns[i])
	}

	/*
	 * Read input file
	 */
	file, err := os.Open("part1.data")
	if err != nil {
		fmt.Println(err)
		return
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	var numbers []int

	for _, line := range lines {
		num, err := strconv.Atoi(line)
		if err != nil {
			fmt.Println(err)
		}
		numbers = append(numbers, num)
	}

	totalFuel := 0
	for _, num := range numbers {
		totalFuel += fuelRequired(num)
	}
	fmt.Println(totalFuel)
}
