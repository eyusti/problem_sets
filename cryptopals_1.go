package main

import "fmt"
import "encoding/hex"
import "encoding/base64"
import "strings"
import "os"
import "bufio"


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
	//const secret = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	//solution_3, _:= problem_3(secret)
	//fmt.Println(solution_3)
	//Problem 4
	const file_name = "set_1_problem_4.txt"
	solution_4:= problem_4(file_name)
	fmt.Println(solution_4)
}

func error_checker(e error){
	if e != nil {
		fmt.Println("** WAS ERROR **")
	}
}

func problem_1(input string)string{
	bytes, err := hex.DecodeString(input)
	error_checker(err)
	solution := base64.StdEncoding.EncodeToString(bytes)
	return solution
}

func problem_2(input_1, input_2 string)string{
	bytes_1, err_1 := hex.DecodeString(input_1)
	bytes_2, err_2 := hex.DecodeString(input_2)

	error_checker(err_1)
	error_checker(err_2)

	length := len(bytes_1)
	var result []byte
	for b:= 0; b < length; b++ {
		result = append(result,bytes_1[b]^bytes_2[b])
	}

	result_encoded := hex.EncodeToString(result)
	return result_encoded
}

func problem_3(input string)(string, int){
	working_bytes, err := hex.DecodeString(input)
	error_checker(err)

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
		c_score += strings.Count(string(decoded)," ")
		c_score -= strings.Count(string(decoded),"\n")
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
	return solution, h_score
}

func problem_4(input string)string{
	file, err := os.Open(input)
	error_checker(err)
	defer file.Close()
	
	var hex_strings []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan(){
		hex_strings = append(hex_strings, scanner.Text())
	}

	h_score := 0
	var best_suggestion string
	for i:= 0; i<len(hex_strings); i++ {
		suggestion, score := problem_3(hex_strings[i])
		//fmt.Println(suggestion)
		//fmt.Println(score)
		if score > h_score {
			h_score = score
			best_suggestion = suggestion
		}
	}
	return best_suggestion
}