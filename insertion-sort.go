package main

import "fmt"


func insertionSort(A []int){
	// keeping track of sort complexity
	initial := make([]int,len(A))
	copy(initial, A)
	var outerCount, innerCount int

	for i := range A {
		outerCount++

		if(i+1 == len(A)){break}
		key := A[i+1]

		j := i // start of left sorted partition
		for (j > -1 &&  key < A[j]){
			innerCount++

			A[j+1] = A[j] // overwrite adjacent position (shifting over unsorted partition)
			j-- // walk down unsorted partition
		}

		A[j+1] = key // j+1 to "undo" stopping condition

		if j != i {
			tmp := make([]int,len(A))
			copy(tmp, A)
			insertionSort(tmp)
		}
	}

	fmt.Println("initial:", initial)
	fmt.Println("outer:",outerCount,"inner:", innerCount,"total:",innerCount+outerCount,"\n============")
}

func main(){
	arr := []int{5,4,3,2,1} // reverse sorted array

	insertionSort(arr)

	println("Done.")
}
