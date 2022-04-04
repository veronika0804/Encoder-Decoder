import collections
import string

alphabet = string.ascii_lowercase
most_common_letter = 'e'
forward_step = 1
back_step = -1
random_letter = 'b'


def keys(input_key, text_list):  #создание ключа
    all_str = ''
    input_key = input_key.lower()

    for i, line in enumerate(text_list): #объединяет всё в одну строку
        if i < len(text_list) - 1:
            all_str += line[:-1] + ' '
        elif i == len(text_list) - 1:
            all_str += line
    i = 0
    j = 0
    key = ''
    while i < len(all_str):
        if all_str[i] in alphabet:
            key += input_key[j % len(input_key)]
            i += 1
            j += 1
        elif all_str[i] not in alphabet:
            key += random_letter
            i += 1
    return key


def caesar(input_txt, output_txt, step, choice):  #шифр Цезаря

    if choice == 'encrypt':
        choice = forward_step
    elif choice == 'decrypt':
        choice = back_step

    with open(input_txt, 'r') as text, open(output_txt, 'w') as code:
        text_list = text.readlines()
        working_line = ''
        code_list = []

        for line in text_list:
            line = line.lower()
            for symbol in line:
                if symbol not in alphabet:
                    working_line += symbol
                else:
                    working_line += alphabet[
                        (alphabet.find(symbol) + step * choice) % len(alphabet)]
            code_list.append(working_line)
            working_line = ''
        for line in code_list:
            code.write(line)
    return code


def caesar_hack(input_txt, output_txt):   #взлом шифра Цезаря

    with open(input_txt, 'r') as code:

        code_list = code.readlines()

        all_letters = ''

        for line in code_list:
            line = line.lower()
            for symbol in line:
                if symbol in alphabet:
                    all_letters += symbol

        most_common_element = \
            collections.Counter(all_letters).most_common(1)[0][0]
        key = alphabet.find(
            most_common_element) - alphabet.find(most_common_letter)

    return caesar(input_txt, output_txt, key, 'decrypt')


def vigenere(input_txt, output_txt, input_key, choice):   #шифр Виженера


    if choice == 'encrypt':
        choice = forward_step
    elif choice == 'decrypt':
        choice = back_step

    with open(input_txt, 'r') as text, open(output_txt, 'w') as code:

        text_list = text.readlines()
        work_line = ''
        code_list = []
        key = keys(input_key, text_list)

        for line in text_list:
            line = line.lower()
            for i, symbol in enumerate(line):
                if symbol not in alphabet:
                    work_line += symbol
                else:
                    work_line += alphabet[(alphabet.find(
                        symbol) + choice * alphabet.find(
                        key[i])) % len(alphabet)]
            code_list.append(work_line)
            work_line = ''
        for line in code_list:
            code.write(line)
    return code


