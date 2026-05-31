# Write a Python program to find the length of the my_str using loop:-
from operator import truediv


# Input:- 'Write a Python program to find the length of the my_str'
# Output:- 55

def length_of_string_using_loop() -> None:
    my_string = 'Write a Python program to find the length of the my_str'
    count = 0

    for ch in my_string:
        count += 1

    print("Total word count : ", count)


# Write a Python program to find the total number of times letter 'p' is appeared in the below string using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.\n'
# Output:- 9


def count_letter_frequency() -> None:
    input_str = 'peter piper picked a peck of pickled peppers.'

    total_count = 0
    for ch in input_str:
        if ch == 'p' or ch == 'P':
            total_count += 1

    print("Total count of letter 'P' : ", total_count)


# Write a Python Program, to print all the indexes of all occurences of letter 'p' appeared in the string using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:-
# 0 # 6  # 8 # 12 # 21 # 29 # 37 # 39 # 40

def print_letter_index_from_string() -> None:
    input_str = 'peter piper picked a peck of pickled peppers.'

    index = 0

    for ch in input_str:
        if ch == 'p' or ch == 'P':
            print(index)
        index += 1


# Write a python program to find below output using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']

def split_and_print_word_using_loop() -> None:
    input_str = 'peter piper picked a peck of pickled peppers.'

    words = []
    word = ''

    for ch in input_str:
        if ch == ' ':
            if word:
                words.append(word)
                word = ''
        else:
            word += ch

    print(words)


# Write a python program to find below output using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'peppers pickled of peck a picked piper peter'

def reverse_string_word_using_loop() -> None:
    input_str = 'peter piper picked a peck of pickled peppers'
    output = ''

    words = input_str.split()

    for i in range(len(words) - 1, -1, -1):
        output += words[i] + " "

    print(output)


# Write a python program to find below output using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- '.sreppep delkcip fo kcep a dekcip repip retep'

def reveres_string_using_loop() -> None:
    input_str = 'peter piper picked a peck of pickled peppers.'

    for i in range(len(input_str) - 1, -1, -1):
        print(input_str[i], end="")

    print("")


# Write a python program to find below output using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'retep repip dekcip a kcep fo delkcip sreppep'

def reverse_word_of_string() -> None:
    input_str = 'peter piper picked a peck of pickled peppers.'
    i = 0
    p_word = 1
    for ch in input_str:
        if ch == " " or i == len(input_str) - 1:
            for j in range(i - 1, i - p_word, -1):
                print(input_str[j], end="")
            print(" ", end="")
            p_word = 0

        i += 1
        p_word += 1


# Write a python program to find below output using loop:-

# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'

def convert_string_camel_case() -> None:
    input_str = 'peter piper picked a peck of pickled peppers.'
    print("")
    word_start = 0

    for char in input_str:
        if word_start == 0:
            print(char.upper(), end="")
            word_start = 1
        else:
            print(char, end="")

        if char == " ":
            word_start = 0


# Write a python program to find below output using loop:-

# Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
# Output:- 'Peter piper picked a peck of pickled peppers'

def convert_camel_case_string_to_lower() -> None:
    input_str = "Peter Piper Picked A Peck Of Pickled Peppers."
    word_start = 0
    start = True
    print("")

    for char in input_str:
        if start:
            print(char, end="")
            start = False
        elif word_start == 0:
            print(char.lower(), end="")
            word_start = 1
        elif char == " ":
            word_start = 0
            print(char, end="")
        else:
            print(char, end="")


# Write a python program to implement index method using loop. If sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-

# Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Pickl'
# Output:- 29

def find_sub_string_index() -> None:
    my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
    sub_str = 'Pickl'

    for i in range(len(my_str) - len(sub_str) + 1):
        match = True

        for j in range(len(sub_str)):
            if my_str[i + j] != sub_str[j]:
                match = False
                break

        if match:
            print("Index of first occurrence:", i)
            break


# Write a python program to implement replace method using loop. If sub_str is found in my_str then it will replace the first
# occurrence of sub_str with new_str else it will print sub_str not found:-

# Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', new_str = 'Pack'
# Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'

def find_sub_string_and_replace() -> None:
    my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
    sub_str = 'Peck'
    new_str = 'Pack'
    found = False

    for i in range(len(my_str) - len(sub_str) + 1):
        match = True

        for j in range(len(sub_str)):
            if my_str[i + j] != sub_str[j]:
                match = False
                break
        if match:
            result = my_str[:i] + new_str + my_str[i + len(new_str):]
            print(result)
            found = True
            break
    if not found:
        print("sub_str not found")


# Write a python program to find below output (implements rjust and ljust) using loop:-

# Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck',
# Output:- '*********************Peck********************'


def find_sub_string_and_replace_with_star() -> None:
    my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
    sub_str = 'Peck'
    new_str = 'Pack'
    found = False

    for i in range(len(my_str) - len(sub_str) + 1):
        match = True

        for j in range(len(sub_str)):
            if my_str[i + j] != sub_str[j]:
                match = False
                break
        if match:
            print(f"{'*' * i} {new_str} {'*' * (i + len(new_str))}")
            found = True
            break
    if not found:
        print("sub_str not found")


# Write a python program to find below output using loop:-

# Input:- 'This is Python class', sep = ' is',
# Output:- ['This', 'is', 'Python class']

def string_to_tuple_convert() -> None:
    input_str = 'This is Python class'
    sep = ' is'
    result_list = []
    found = False

    for i in range(len(input_str) - len(sep) + 1):
        match = True

        for j in range(len(sep)):
            if input_str[i + j] != sep[j]:
                match = False
                break

        if match:
            result_list.append(input_str[:i])
            result_list.append(sep.strip())
            result_list.append(input_str[i + len(sep):].strip())
            found = True
            break

    if not found:
        result_list.append(input_str)

    print(result_list)


if __name__ == "__main__":
    length_of_string_using_loop()
    count_letter_frequency()
    print_letter_index_from_string()
    split_and_print_word_using_loop()
    reverse_string_word_using_loop()
    reveres_string_using_loop()
    reverse_word_of_string()
    convert_string_camel_case()
    convert_camel_case_string_to_lower()
    print()
    find_sub_string_index()
    find_sub_string_and_replace()
    find_sub_string_and_replace_with_star()
    string_to_tuple_convert()
