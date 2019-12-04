package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func FuelRequired(mass int) int {
	fuel := mass / 3
	fuel = int(fuel)
	return fuel - 2
}

func PartOne(numbers []int) int {
	totalFuel := 0
	for _, num := range numbers {
		totalFuel += FuelRequired(num)
	}
	return totalFuel

}

func FuelRequiredIncludingFuel(mass int) int {
	fuel := FuelRequired(mass)
	if fuel >= 0 {
		fuel += FuelRequiredIncludingFuel(fuel)
	} else {
		fuel = 0
	}
	return fuel
}

func PartTwo(numbers []int) int {
	totalFuel := 0
	for _, num := range numbers {
		totalFuel += FuelRequiredIncludingFuel(num)
	}
	return totalFuel
}

func main() {
	/*
	 * Test givens
	 */
	test1Input := [4]int{12, 14, 1969, 100756}
	test1Ans := [4]int{2, 2, 654, 33583}
	test2Input := [4]int{12, 1969, 100756}
	test2Ans := [4]int{2, 966, 50346}

	for i := 0; i < len(test1Input); i++ {
		val := FuelRequired(test1Input[i])
		fmt.Printf("%d returned %d: %t\n", test1Input[i], val, val == test1Ans[i])
	}

	for i := 0; i < len(test2Input); i++ {
		val := FuelRequiredIncludingFuel(test2Input[i])
		fmt.Printf("%d returned %d: %t\n", test2Input[i], val, val == test2Ans[i])
	}

	/*
	 * Read input file
	 */
	file, err := os.Open("data.txt")
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

	fmt.Println(PartOne(numbers))
	fmt.Println(PartTwo(numbers))

}
