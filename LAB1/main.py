#EXERCITIU 1
def gcd(n1,n2):
    if n2 == 0:
        return n1
    return gcd(n2,n1 % n2)

def final_gcd(numbers):
    result = 1
    for index in range(1,len(numbers)):
        if index == 1:
            result = gcd(numbers[index-1],numbers[index])
        else:
            result = gcd(result,numbers[index])
    return result

numbers = [int(x) for x in input().split()]
print(final_gcd(numbers))


#EXERCITIU 2
def how_many_vowels (s):
    counter = 0
    vowels = "aeiouAEIOU"
    for index in range (0,len(s)):
        if s[index] in vowels:
            counter = counter + 1
    return counter

print(how_many_vowels("asfAEasgki"))


#EXERCITIU 3
def number_of_occurences (s1, s2):
    counter = 0
    for index in range(0,len(s2)):
        aux = s2[index : index + len(s1)]
        if aux == s1:
            counter = counter + 1
    return counter

print(number_of_occurences("ab","abcdabb"))


#EXERCITIU 4
def upper_to_lowercase_underscore(s):
    final = ""
    for index in range(0,len(s)):
        if "A" <= s[index] <= "Z":
            final = final + "_"
            final = final + s[index].lower()
        else:
            final = final + s[index]
    return final[1:]

print(upper_to_lowercase_underscore("MergeDa"))


#EXERCITIU 5
def spiral_order(matrix, i,j,m,n):
    result = ""
    while i < m and j < n:
        for index in range(j, n):
            result += matrix[i][index]
        for index in range(i + 1, m):
            result += matrix[index][n - 1]
        if i < m - 1:
            for index in range(n - 2, j - 1, -1):
                result += matrix[m - 1][index]
        if j < n - 1:
            for index in range(m - 2, i, -1):
                result += matrix[index][j]
        i += 1
        j += 1
        m -= 1
        n -= 1
    return result

matrix = [["f","i","r","s"],["n","_","l","t"],["o","b","a","_"],["h","t","y","p"]]
print(spiral_order(matrix,0,0,4,4))


#EXERCITIU 6
def palindrome(n):
    s = str(n)
    for index in range(0,len(s)):
        if s[index] != s[-index-1]:
            return 0
    return 1

print(palindrome(31213))


#EXERCITIU 7
def extract_number(s):
    number = 0
    flag = 0
    for index in range(0,len(s)):
        if s[index].isdigit() and flag == 0:
            flag = 1
            for index_digit in range(index, len(s)):
                if s[index_digit].isdigit():
                    number = number * 10 + (ord(s[index_digit]) - ord("0"))
                else:
                    return number
    return number

print(extract_number("An apple is 123 USD"))


#EXERCITIU 8
def how_many_bits(n):
    binary = bin(n)
    s = str(binary)
    counter = 0
    for index in range(0,len(s)):
        if s[index] == "1":
            counter = counter + 1
    return counter

print(how_many_bits(24))


#EXERCITIU 9
def most_common_letter(s):
    freq_lowercase = []
    freq_uppercase = []
    for index in range(ord("a")-ord("a"),ord("z")-ord("a")):
        freq_lowercase.append(0)
        freq_uppercase.append(0)

    for index in range(0,len(s)):
        if s[index].isupper():
            freq_uppercase[ord(s[index])-ord("A")] = freq_uppercase[ord(s[index])-ord("A")] + 1
        elif s[index].islower():
            freq_lowercase[ord(s[index])-ord("a")] = freq_lowercase[ord(s[index])-ord("a")] + 1

    max = 0
    letter = ""

    for index in range(ord("a")-ord("a"),ord("z")-ord("a")):
        if freq_lowercase[index] > max:
            max = freq_lowercase[index]
            letter = chr(index + ord("a"))
        if freq_uppercase[index] > max:
            max = freq_lowercase[index]
            letter = chr(index + ord("A"))
    return letter

print(most_common_letter("an apple is not a tomato"))


#EXERCITIU 10
def how_many_words(s):
    counter = 0
    for index in range(0,len(s)):
        if s[index] == " ":
            counter = counter + 1
    return counter + 1

print(how_many_words("I have Python exam"))