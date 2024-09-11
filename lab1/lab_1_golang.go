package main

import (
	"os"
	"strconv"
)

func getCoef(index int, prompt string) (int, error){
	for{
		coefStr := os.Args[index]
		coef, err := strconv.ParseFloat(coefStr, 64)
		
	}
}

func main(){

}