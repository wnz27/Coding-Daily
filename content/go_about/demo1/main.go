/*
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2023-08-18 00:08:36
 * @LastEditTime: 2023-08-18 00:12:30
 * @FilePath: /Coding-Daily/content/go_about/demo1/main.go
 * @description: type some description
 */
package main

import (
	"fmt"
	"sync"
)

const maxSize = 46

var caches [maxSize]sync.Pool

func t1() {
	for i := 0; i < maxSize; i++ {
		// 翻倍
		size := 1 << i
		// caches[i].New = func() interface{} {
		// 	buf := make([]byte, 0, size)
		// 	return buf
		// }
		fmt.Println(size)
	}
}

func main() {
	t1()
	// for k, v := range caches {
	// 	fmt.Println(k, v)
	// }
}
