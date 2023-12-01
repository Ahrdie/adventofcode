package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func main() {
  input := `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`
	inputLines := strings.Split(input, "\n")
	calibrationValues := 0

	for _, line := range inputLines {
		re := regexp.MustCompile(`[0-9]`)
		finds := re.FindAll([]byte(line), -1)
		firstdigit, err := strconv.Atoi(string(finds[0]))
    if err != nil {
        panic(err)
    }
		lastdigit, err := strconv.Atoi(string(finds[len(finds)-1]))
    if err != nil {
        panic(err)
    }

		println(line, firstdigit)
		calibrationValues += firstdigit*10+lastdigit
		fmt.Print(calibrationValues)
	}
}