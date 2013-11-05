package main

import (
    "fmt"
    "math/rand"
    "math"
	"math/cmplx"
)

func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
    fmt.Println("My favorite number is", rand.Intn(10))
    fmt.Printf("Now you have %g problems.\n", math.Pi)
    constants()
}

var (
    ToBe   bool       = false
    MaxInt uint64     = 1<<64 - 1
    z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func constants() {
    const f = "%T(%v)\n"
    fmt.Printf(f, ToBe, ToBe)
    fmt.Printf(f, MaxInt, MaxInt)
    fmt.Printf(f, z, z)
}
