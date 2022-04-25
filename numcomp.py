# [2021-07-05] Challenge #397 [Easy] Roman numeral comparison
# https://www.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

# dictionary to hold roman numeral values
roman_nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

# Function to convert roman numerals to base 10 numbers
def roman_to_num(num):
    rsp = sum([roman_nums.get(x.upper()) for x in list(num)])
    return rsp

# Funciton to compare roman numeral values
def numcomp(num1, num2):
    return roman_to_num(num1) < roman_to_num(num2)

if __name__ == '__main__':
    print("I < I: " + str(numcomp("I", "I")))
    print("I < II: " + str(numcomp("I", "II")))
    print("II < I: " + str(numcomp("II", "I")))
    print("V < IIII: " + str(numcomp("V", "IIII")))
    print("MDCLXV < MDCLXVI: " + str(numcomp("MDCLXV", "MDCLXVI")))
    print("MM < MDCCCCLXXXXVIIII: " + str(numcomp("MM", "MDCCCCLXXXXVIIII")))
