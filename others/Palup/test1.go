package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

// Node represents a single node in the linked list
type Node struct {
	Value interface{}
	Next  *Node
}

// RequestBody represents the expected JSON input
type RequestBody struct {
	Array []interface{} `json:"Array"`
}

func arrayToLinkedList(array []interface{}) *Node {
	dummy := &Node{}
	curr := dummy
	for _, value := range array {
		curr.Next = &Node{Value: value}
		curr = curr.Next
	}
	return dummy.Next
}

func printLinkedList(w http.ResponseWriter, linkedList *Node) {
	isHead := true
	for linkedList != nil {
		label := "node"
		if isHead {
			label = "head"
			isHead = false
		} else if linkedList.Next == nil {
			label = "tail"
		}

		fmt.Fprintf(w, "%s -> %v\n", label, linkedList.Value)
		linkedList = linkedList.Next
	}
}

func Test1(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Test 1:\n")

	var requestBody RequestBody
	if err := json.NewDecoder(r.Body).Decode(&requestBody); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	linkedList := arrayToLinkedList(requestBody.Array)
	printLinkedList(w, linkedList)
}
