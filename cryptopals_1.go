package main

import "fmt"
import "encoding/hex"
import "encoding/base64"


func main(){
	// Problem 1
	//const i = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	//solution_1 := problem_1(i)
	//fmt.Println(solution_1)
	// Problem 2
	//const one = "1c0111001f010100061a024b53535009181c"
	//const two = "686974207468652062756c6c277320657965" 
	//problem_2(one,two)
	//solution_2 := problem_2(one, two)
	//fmt.Println(solution_2)
	// Problem 3
}
// ask about hex decoding and base 64 encoding
func problem_1(input string)string{
	bytes, err := hex.DecodeString(input)
	if err != nil {
		fmt.Println("** WAS ERROR **")
	}
	solution := base64.StdEncoding.EncodeToString(bytes)
	return solution
}

func problem_2(input_1, input_2 string)string{
	bytes_1, err_1 := hex.DecodeString(input_1)
	bytes_2, err_2 := hex.DecodeString(input_2)
	if err_1 != nil|| err_2 != nil {
		fmt.Println("** WAS ERROR **")
	}
	length := len(bytes_1)
	var result []byte
	for b:= 0; b < length; b++ {
		result = append(result,bytes_1[b]^bytes_2[b])
	}
	result_encoded := hex.EncodeToString(result)
	return result_encoded
}

