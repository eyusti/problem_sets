package main

import "fmt"
import "bytes"
import "encoding/hex"
import "encoding/base64"
import "strings"
import "os"
import "bufio"
import "math/bits"
import "math"
import "unicode"

func main() {
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
	//const file_name = "set_1_problem_4.txt"
	//solution_4:= problem_4(file_name)
	//fmt.Println(solution_4)
	//Problem 5
	//const stanza = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	//solution_5 := problem_5(stanza)
	//fmt.Println(solution_5)
	//Problem 6
	const file_name = "set_1_problem_6.txt"
	solution_6 := problem_6(file_name)
	fmt.Println(solution_6)

}

// Helper functions
func error_checker(e error) {
	if e != nil {
		fmt.Println("** WAS ERROR **")
	}
}

func hamming_distance(bytes_1, bytes_2 []byte) int {
	var total int
	for b := 0; b < len(bytes_1); b++ {
		xored_bytes := bytes_1[b] ^ bytes_2[b]
		difference := bits.OnesCount8(xored_bytes)
		total += difference
	}
	return total
}

func frequency_score(proposed_bytes []byte) float64 {
	expected_frequency := map[byte]float64{
		' ':  0.16667,
		'e':  0.12702,
		't':  0.09,
		'a':  0.081,
		'o':  0.075,
		'i':  0.069,
		'n':  0.06749,
		's':  0.06327,
		'h':  0.06094,
		'r':  0.05987,
		'd':  0.04253,
		'l':  0.04025,
		'u':  0.02758,
		'w':  0.02560,
		'm':  0.02406,
		'f':  0.02228,
		'c':  0.02202,
		'g':  0.02015,
		'y':  0.01994,
		'p':  0.01929,
		'b':  0.01492,
		'k':  0.01292,
		'v':  0.00978,
		'\n': 0,
		'\'': 0,
	}

	score := 0.0
	total := float64(len(proposed_bytes))
	for letter, expected := range expected_frequency {
		upper := byte(unicode.ToUpper(rune(letter)))
		actual := float64(bytes.Count(proposed_bytes, []byte{letter})+bytes.Count(proposed_bytes, []byte{upper})) / total
		score += math.Abs(actual - expected)
	}
	for _, proposed_byte := range proposed_bytes {
		_, ok := expected_frequency[proposed_byte]
		lower := byte(unicode.ToLower(rune(proposed_byte)))
		_, ok2 := expected_frequency[lower]
		if !(ok || ok2) {
			score += 10
		}

	}
	return score
}

func decrypt_repeated_xor(solved_keysize int, list_of_bytes []byte) []byte {
	//transforms text to keysized blocks
	var keysize_mapping map[int][]byte
	keysize_mapping = make(map[int][]byte)
	for i := 0; i < solved_keysize; i++ {
		temp := []byte{}
		for p := i; p < len(list_of_bytes); p += solved_keysize {
			temp = append(temp, list_of_bytes[p])
		}
		keysize_mapping[i] = temp
	}

	// returns mapping with most likely transformation
	var solution_mapping map[int][]byte
	solution_mapping = make(map[int][]byte)
	var solution []byte

	for k := 0; k < solved_keysize; k++ {
		m_score := 1000000.0
		//c_saved := byte(0)
		for c := byte(0); ; c++ {
			decoded := []byte{}
			for i := 0; i < len(keysize_mapping[k]); i++ {
				decoded = append(decoded, c^keysize_mapping[k][i])
			}
			c_score := frequency_score(decoded)
			if c_score < m_score {

				solution = decoded
				m_score = c_score
				//c_saved = c
			}
			decoded = nil
			c_score = 0
			if c == 255 {
				break
			}
		}
		solution_mapping[k] = solution
		m_score = 1000000
	}

	// Decodes from mapping
	var solved_byte_string []byte
	for b := 0; b < len(solution_mapping[0]); b++ {
		for i := 0; i < solved_keysize; i++ {
			if b < len(solution_mapping[i]) {
				solved_byte_string = append(solved_byte_string, solution_mapping[i][b])
			}
		}
	}
	return solved_byte_string
}

// Problems
func problem_1(input string) string {
	bytes, err := hex.DecodeString(input)
	error_checker(err)
	solution := base64.StdEncoding.EncodeToString(bytes)
	return solution
}

func problem_2(input_1, input_2 string) string {
	bytes_1, err_1 := hex.DecodeString(input_1)
	bytes_2, err_2 := hex.DecodeString(input_2)

	error_checker(err_1)
	error_checker(err_2)

	length := len(bytes_1)
	var result []byte
	for b := 0; b < length; b++ {
		result = append(result, bytes_1[b]^bytes_2[b])
	}

	result_encoded := hex.EncodeToString(result)
	return result_encoded
}

//Should make this frequency check better
func problem_3(input string) (string, int) {
	working_bytes, err := hex.DecodeString(input)
	error_checker(err)

	var decoded []byte
	c_score := 0
	h_score := 0
	var solution string
	for c := byte(0); ; c++ {
		for i := 0; i < len(working_bytes); i++ {
			decoded = append(decoded, c^working_bytes[i])
		}
		c_score += strings.Count(string(decoded), "a")
		c_score += strings.Count(string(decoded), "e")
		c_score += strings.Count(string(decoded), "i")
		c_score += strings.Count(string(decoded), "o")
		c_score += strings.Count(string(decoded), "u")
		c_score += strings.Count(string(decoded), " ")
		c_score -= strings.Count(string(decoded), "\n")
		if c_score > h_score {
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

func problem_4(input string) string {
	file, err := os.Open(input)
	error_checker(err)
	defer file.Close()

	var hex_strings []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		hex_strings = append(hex_strings, scanner.Text())
	}

	h_score := 0
	var best_suggestion string
	for i := 0; i < len(hex_strings); i++ {
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

func problem_5(input string) string {
	var stanza_list []byte
	for i := 0; i < len(input); i++ {
		stanza_list = append(stanza_list, input[i])
	}

	ice_ice_bytes := []byte("ICE")
	var xored_list []byte
	index := 0
	for i := 0; i < len(stanza_list); i++ {
		xored_list = append(xored_list, stanza_list[i]^ice_ice_bytes[index])
		if index == 2 {
			index = 0
		} else {
			index += 1
		}
	}
	solution := hex.EncodeToString(xored_list)
	return solution
}

func problem_6(input string) string {
	//opens file and reads lines and converts to list of bytes
	file, err := os.Open(input)
	error_checker(err)
	defer file.Close()
	var lines_from_input []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines_from_input = append(lines_from_input, scanner.Text())
	}
	joined_lines := strings.Join(lines_from_input, "")
	list_of_bytes, err := base64.StdEncoding.DecodeString(joined_lines)
	error_checker(err)

	//predicts keysize
	var solved_keysize int
	min_hamming_distance := 127.0
	for keysize := 2; keysize <= 40; keysize++ {
		first_keysized_bytes := list_of_bytes[:keysize*4]
		second_keysized_bytes := list_of_bytes[keysize*4 : keysize*8]
		hamming_distance := float64(hamming_distance(first_keysized_bytes, second_keysized_bytes))
		if hamming_distance/float64(keysize*4) < min_hamming_distance {
			min_hamming_distance = hamming_distance / float64(keysize*4)
			solved_keysize = keysize
		}
	}
	solution := decrypt_repeated_xor(solved_keysize, list_of_bytes)
	return string(solution)
}
