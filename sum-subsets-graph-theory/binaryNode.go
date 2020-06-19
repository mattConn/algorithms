package main

// binary node
type Node struct {
	data, depth int
	left        *Node
	right       *Node
}

// descend tree
func (n *Node) Descend(nHandler ...func(int, int)) {
	if n == nil {
		return
	}

	for _, f := range nHandler {
		if f != nil {
			f(n.data, n.depth)
		}
	}

	n.left.Descend(nHandler...)
	n.right.Descend(nHandler...)
}

func (n *Node) SumSubsets(l []int, i int) {
	// if end of slice
	if i == len(l) {
		return
	}

	n.left = &Node{data: n.data + l[i], depth: i + 1}
	n.right = &Node{data: n.data, depth: i + 1}

	n.left.SumSubsets(l, i+1)
	n.right.SumSubsets(l, i+1)
}

func (n *Node) MakeSumTree(nums []int) [][]int {
	treeData := make([][]int, len(nums)+1)

	// populate tree
	n.SumSubsets(nums[:], 0)

	// populate array
	n.Descend(func(val, depth int) { treeData[depth] = append(treeData[depth], val) })

	return treeData
}
