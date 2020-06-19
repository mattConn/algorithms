package main

import (
	"html/template"
	"log"
	"net/http"
	"strconv"
	"strings"
	"time"
)

type tree struct {
	Data        [][]int
	Input       []int
	TimeElapsed time.Duration
}

func handler(w http.ResponseWriter, r *http.Request) {
	inputArr := strings.Split(r.FormValue("body"), " ")
	nums := []int{}
	for _, v := range inputArr {
		n, _ := strconv.Atoi(v)
		nums = append(nums, n)
	}

	N := Node{}

	t, _ := template.ParseFiles("index.html")
	start := time.Now()
	t.Execute(w, tree{Data: N.MakeSumTree(nums), Input: nums, TimeElapsed: time.Since(start)})
}

func main() {
	http.Handle("/assets/", http.StripPrefix("/assets/", http.FileServer(http.Dir("assets"))))
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
