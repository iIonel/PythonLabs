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

fibo = int(input("First fibonnaci numbers: "))
print(first_fibonacci(fibo - 1))


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

print("List of numbers: ")
numbers = [int(x) for x in input().split()]
print(main_function(numbers))


#EXERCITIU 3
print("List A: ")
list_a = [x for x in input().split()]
print("List B: ")
list_b = [x for x in input().split()]

print("Intersection: ")
print([x for x in list_a if x in list_b])
print("Union: ")
print(list(list_a + [x for x in list_b if x not in list_a]))
print("A-B: ")
print([x for x in list_a if x not in list_b])
print("B-A: ")
print([x for x in list_b if x not in list_a])


#EXERCITIU 4
def compose(notes, positions,start):
    final = []
    final.append(notes[start])
    for index in range(0,len(positions)):
        start = (start + positions[index]) % len(notes)
        final.append(notes[start])
    return final

print("Notes: ")
notes = [x for x in input().split()]
print("Positions: ")
positions = [int(x) for x in input().split()]
start = int(input("Start position: "))

print(compose(notes, positions, start))


#EXERCITIU 5
def replace_with_zeros(matrix):
    rows = len (matrix)
    columns = len(matrix[0])
    for i in range(0, rows):
        for j in range(0,columns):
            if j < i:
                matrix[i][j] = 0
    return matrix

i = int(input("Number of rows: "))
j = int(input("Number of columns: "))

matrix = []
for r in range(0,i):
    row = []
    for c in range(0,j):
        row.append(int(input()))
    matrix.append(row)

matrix = replace_with_zeros(matrix)
for r in range(0,i):
    for c in range(0,j):
        print(matrix[r][c],end=" ")
    print()


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

n = int(input("Number of lists: "))
lists = []
for i in range(0,n):
    curr_list = [x for x in input().split()]
    lists.append(curr_list)

x = int(input("Exactly times: "))
print(exactly_x_items(lists,x))


#EXERCITIU 7
def palindrome(n):
    s = str(n)
    for index in range(0,len(s)):
        if s[index] != s[-index-1]:
            return 0
    return 1

def tuple_list(list):
    final_list = [x for x in list if palindrome(x) == 1]
    palindrom_tuple = (len(final_list),max(final_list))
    return palindrom_tuple

print("List: ")
list = [int(x) for x in input().split()]
print(tuple_list(list))


#EXERCITIU 8
def generate_list(x, strings, flag):
    a = []
    for i in range(0, len(strings)):
        b = []
        for j in range(0, len(strings[i])):
            if ord(strings[i][j]) % x == 0 and flag:
                b.append(strings[i][j])
            if ord(strings[i][j]) % x != 0 and not flag:
                b.append(strings[i][j])
        if len(b) > 0:
            a.append(b)
    return a

x = int(input("Divisible by: "))
print("My strings: ")
strings = [list(x) for x in input().split()]
flag_input = input("My flag (True/False): ")
flag = flag_input.lower() == "true"
final_list = generate_list(x, strings, flag)
print("Final list:", final_list)


#EXERCITIU 9
def list_tuples(matrix):
    final_list = []
    for i in range(1,len(matrix)):
        for j in range(0,len(matrix[0])):
            for r in range(0, i):
                if matrix[r][j] >= matrix[i][j]:
                    tuple = (i,j)
                    final_list.append(tuple)
                    break
    return final_list

n = int(input("Rows: "))
m = int(input("Columns: "))
matrix = []
for i in range(0,n):
    row = []
    for j in range(0,m):
        row.append(int(input()))
    matrix.append(row)
print(list_tuples(matrix))


#EXERCITIU 10
def elements_tuple(lists):
    x = max([len(x) for x in lists])

    final_lists = []
    for i in range(x):
        tuple_list = tuple(lists[j][i] if i < len(lists[j]) else None for j in range(len(lists)))
        final_lists.append(tuple_list)
    return final_lists

n = int(input("Number of lists: "))
lists = []
for i in range(n):
    current_list = [x for x in input().split()]
    lists.append(current_list)
final_result = elements_tuple(lists)
print(final_result)


#EXERCITIU 11
def order_list(lists):
    return sorted(lists, key=lambda x: x[1][2])

n = int(input("Number of lists: "))
lists = []
for i in range(n):
    tuple_list = tuple(x for x in input().split())
    lists.append(tuple_list)
final = print(order_list(lists))


#EXERCITIU 12
def result_group(group):
    group = sorted(group, key=lambda x: x[-2:])
    i = 0
    final_list = []

    while i < len(group):
        j = i + 1
        ok = 1
        tuple_list = [group[i]]

        while ok == 1 and j < len(group):
            if group[j][-2:] != group[i][-2:]:
                i = j
                ok = 0
                tuple_list = tuple(tuple_list)
                final_list.append(tuple_list)
            else:
                tuple_list.append(group[j])
            j = j + 1
        if ok == 1:
            i = j

    return final_list

print("List of words: ")
group_by_rhyme = input().split()
result = result_group(group_by_rhyme)
print(result)