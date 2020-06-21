package main

import (
	"fmt"
	"os/exec"
	"strconv"
)

// make array-based binary tree for sums of subsets of input
func fillSumTree (input, output []int, n, i int) {
	// i = input index, n = output index
	if( i == len(input)){
		return
	}

	output[2*n+1] = output[n]+input[i] // left node
	output[2*n+2] = output[n] // right node

	// i+1 for each call to match depth
	fillSumTree(input,output,2*n+1,i+1) // descend left 
	fillSumTree(input,output,2*n+2,i+1) // descend right
}

func main(){
	nums := []int{2,4,6}
	output := make([]int, 1<<(len(nums)+1)-1) // accomodate all nodes for breadth-first representation
	fmt.Println(len(output))

	fillSumTree(nums,output,0,0)

	outputString := []string{}

	for _,v := range output {
		outputString = append(outputString,strconv.Itoa(v))
	}

	err := exec.Command("./graph-plotter.py", outputString...).Run()
	if err != nil {
		fmt.Println(err)
	}
}
