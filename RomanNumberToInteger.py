class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        result = 0
        prev_value = 0  

        for i in range(len(s)):
            current_value = roman_numerals[s[i]]
            if current_value > prev_value:
                result += current_value - 2 * prev_value 
            else:
                result += current_value
            prev_value = current_value 

        return result

  #leetcode problem, by Mehdi Khoudali
