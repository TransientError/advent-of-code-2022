package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"kvwu.io/advent-of-code/utils"
)

type Point = [2]int

func move(point Point, direction string) Point {
	x := point[0]
	y := point[1]

	switch direction {
	case "R":
		return [2]int{x + 1, y}
	case "L":
		return [2]int{x - 1, y}
	case "D":
		return [2]int{x, y - 1}
	case "U":
		return [2]int{x, y + 1}
	case "":
		return point
	case "UR":
		return [2]int{x + 1, y + 1}
	case "UL":
		return [2]int{x - 1, y + 1}
	case "DR":
		return [2]int{x + 1, y - 1}
	case "DL":
		return [2]int{x - 1, y - 1}
	}

	panic("not reachable")
}

func calculateTailMove(head Point, tail Point) string {
	h_x := head[0]
	h_y := head[1]
	t_x := tail[0]
	t_y := tail[1]

	x_distance := h_x - t_x
	y_distance := h_y - t_y

	if x_distance <= 1 && y_distance <= 1 && x_distance >= -1 && y_distance >= -1 {
		return ""
	}

	if x_distance > 0 && y_distance > 1 || x_distance > 1 && y_distance > 0 {
		return "UR"
	}

	if x_distance > 0 && y_distance < -1 || x_distance > 1 && y_distance < 0 {
		return "DR"
	}
	
	if x_distance < -1 && y_distance > 0 || x_distance < 0 && y_distance > 1 {
		return "UL"
	}

	if x_distance < -1 && y_distance < 0 || x_distance < 0 && y_distance < -1 {
		return "DL"
	}

	if y_distance < -1 {
		return "D"
	}

	if x_distance < -1 {
		return "L"
	}

	if x_distance > 1 {
		return "R"
	}

	if y_distance > 1 {
		return "U"
	}

	panic("not reachable")
}

func main() {
	data := string(utils.JustRun(func() ([]byte, error) { return os.ReadFile("input.txt") }))

	lines := strings.Split(data, "\n")
	
	head := [2]int{0, 0}
	tail := [2]int{0, 0}

	visited := make(map[Point] bool)

	visited[tail] = true

	for _, line := range lines {
		if line != "" {
			parsed := strings.Split(line, " ")
			direction := parsed[0]
			steps := utils.JustRun(func() (int, error) { return strconv.Atoi(parsed[1]) })

			for steps > 0 {
				head = move(head, direction)
				tail_direction := calculateTailMove(head, tail)
				tail = move(tail, tail_direction)

				visited[tail] = true
				steps--
			}
		}
	}

	fmt.Println(len(visited))
}



