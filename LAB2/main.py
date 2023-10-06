#EXERCITIU 1
import math
def first_fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    list = first_fibonacci(n - 1)
    list.append(list[-2] + list[-1])
    return list

print(first_fibonacci(10))


#EXERCITIU 2
def prime_check(n):
    if n < 0:
        n = abs(n)
    if n == 0 or n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    elif n % 2 == 0:
        return 0
    for div in range(3,int(math.sqrt(n)),2):
        if n % div == 0:
            return 0
    return 1

def main_function(numbers):
    x = [x for x in numbers if prime_check(x) == 1]
    return x

print(main_function([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))


#EXERCITIU 3



#EXERCITIU 4
def compose(notes, positions,start):
    final = []
    final.append(notes[start])
    for index in range(0,len(positions)):
        start = (start + positions[index]) % len(notes)
        final.append(notes[start])
    return final

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


#EXERCITIU 5
def replace_with_zeros(matrix):
    rows = len (matrix)
    columns = len(matrix[0])
    for i in range(0, rows):
        for j in range(0,columns):
            if j < i:
                matrix[i][j] = 0
    return matrix

matrix = replace_with_zeros([
    [3, 10, 2],
    [1, 5, 0],
    [73, 12, 91]
])

print(matrix)


#EXERCITIU 6
def dinstinct_compute(list):
    dinstinct = []
    for x in list:
        if list.count(x) > 1:
            if dinstinct.count(x) == 0:
                dinstinct.append(x)
        else:
            dinstinct.append(x)
    return dinstinct

def compute(lists):
    all_lists = []
    for list in lists:
        all_lists.extend(list)
    return all_lists

def exactly_x_items(lists, x):
    items = []
    list = compute(lists)
    dinstinct = dinstinct_compute(list)
    for number in dinstinct:
        if list.count(number) == x:
            items.append(number)
    return items

lists = [[1,2,3], [2,3,4],[4,5,6],[4,1, "test"]]
print(exactly_x_items(lists,2))


#EXERCITIU 7
def palindrome(n):
    s = str(n)
    for index in range(0,len(s)):
        if s[index] != s[-index-1]:
            return 0
    return 1

def tuple_list(list):
    final_list = []
    for number in list:
        if palindrome(number) == 1:
            final_list.append(number)
    palindrom_tuple = (len(final_list),max(final_list))
    return palindrom_tuple

print(tuple_list([1,2,3,4,121,54,14141]))


#EXERCITIU 8



#EXERCITIU 9



#EXERCITIU 10



#EXERCITIU 11



#EXERCITIU 12