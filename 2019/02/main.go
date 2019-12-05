package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func OpCodeOne(input []int, opIndex int) []int {
	input[input[opIndex+3]] = input[input[opIndex+1]] + input[input[opIndex+2]]
	return input
}

func OpCodeTwo(input []int, opIndex int) []int {
	input[input[opIndex+3]] = input[input[opIndex+1]] * input[input[opIndex+2]]
	return input
}

func ProcessOpCodes(input []int) []int {
	i := 0
	for i < len(input) {
		switch val := input[i]; val {
		case 1:
			input = OpCodeOne(input, i)
		case 2:
			input = OpCodeTwo(input, i)
		case 99:
			break
		default:
			fmt.Printf("Incorrect opcode %d found as position %d\n", input[i], i)
		}
		i += 4
	}
	return input
}

func PartOne(input []int) int {
	var testInput = make([]int, len(input))
	copy(testInput, input)
	testInput[1] = 12
	testInput[2] = 2
	testInput = ProcessOpCodes(testInput)
	return testInput[0]
}

func PartTwo(input []int) int {
	for noun := 0; noun <= 99; noun++ {
		for verb := 0; verb <= 99; verb++ {
			var test = make([]int, len(input))
			copy(test, input)
			test[1] = noun
			test[2] = verb
			if ProcessOpCodes(test)[0] == 19690720 {
				return noun*100 + verb
			}
		}
	}
	return -1
}

func GetInput() []int {
	bytes, _ := ioutil.ReadFile("data.txt")
	var input []int
	for _, s := range strings.Split(string(bytes), ",") {
		num, _ := strconv.Atoi(s)
		input = append(input, num)
	}
	return input
}
func main() {
	test1Input1 := []int{1, 0, 0, 0, 99}
	fmt.Println(ProcessOpCodes(test1Input1))
	test1Input2 := []int{2, 3, 0, 3, 99}
	fmt.Println(ProcessOpCodes(test1Input2))
	test1Input3 := []int{2, 4, 4, 5, 99, 0}
	fmt.Println(ProcessOpCodes(test1Input3))
	test1Input4 := []int{1, 1, 1, 4, 99, 5, 6, 0, 99}
	fmt.Println(ProcessOpCodes(test1Input4))

	input := GetInput()

	fmt.Printf("Answer to part 1: %d\n", PartOne(input))
	fmt.Printf("Answer to part 2: %d\n", PartTwo(input))
}
