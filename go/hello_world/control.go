package main

import "fmt"

func main() {

	for_loop()
	while_loop()
	range_iter()
}

func for_loop () {
    sum := 0
    for i := 0; i < 10; i++ {
        sum += i
    }
    fmt.Println(sum)

}

func while_loop () {
    sum := 1
    for sum < 1000 {
        sum += sum
    }
    fmt.Println(sum)

}



func range_iter() {
    pow := []int{1, 2, 4, 8, 16, 32, 64, 128}

    for i, v := range pow {
        fmt.Printf("2**%d = %d\n", i, v)
    }

    pow = make([]int, 10)
    for i := range pow {
        pow[i] = 1 << uint(i)
    }
    for _, value := range pow {
        fmt.Printf("%d\n", value)
    }
}
