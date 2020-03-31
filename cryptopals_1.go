package main

import "fmt"
import "encoding/hex"
import "encoding/base64"
import "strings"


func main(){
	// Problem 1
	//const i = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	//solution_1 := problem_1(i)
	//fmt.Println(solution_1)
	// Problem 2
	//const one = "1c0111001f010100061a024b53535009181c"
	//const two = "686974207468652062756c6c277320657965" 
	//solution_2 := problem_2(one, two)
	//fmt.Println(solution_2)
	// Problem 3
	const secret = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	solution_3:= problem_3(secret)
	fmt.Println(solution_3)
	//solution_3 := problem_3(secret)
	//fmt.Println(solution_3)
}

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

func problem_3(input string)string{
	working_bytes, err := hex.DecodeString(input)
	if err != nil {
		fmt.Println("** WAS ERROR **")
	}

	var decoded []byte
	c_score := 0
	h_score := 0
	var solution string
	for c:= byte(0); ; c++ {
		for i:=0; i < len(working_bytes); i++ {
			decoded = append(decoded,c^working_bytes[i])
		}
		c_score += strings.Count(string(decoded),"a")
		c_score += strings.Count(string(decoded),"e")
		c_score += strings.Count(string(decoded),"i")
		c_score += strings.Count(string(decoded),"o")
		c_score += strings.Count(string(decoded),"u")
		if c_score > h_score{
			solution = string(decoded)
			h_score = c_score
		}
		if c == 255 {
			break
		}
		decoded = nil
		c_score = 0
	}
	return solution
}