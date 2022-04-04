from func import caesar_hack
from func import caesar, vigenere


def caesar_work():
    choice = input(
        'e - encrypt, d - decrypt, h - hack\n')
    input_file = input('print files name for encryption\n')
    output_file = input('print output file name\n')
    if choice == 'h':
        return caesar_hack(input_file, output_file)
    key = int(input('print key(number)\n'))
    if choice == 'e':
        return caesar(input_file, output_file, key, 'encrypt')
    elif choice == 'd':
        return caesar(input_file, output_file, key, 'decrypt')


def vigenere_work():
    choice = input('e - encrypt, d - decrypt\n')
    input_file = input('print files name for encryption\n')
    output_file = input('print output file name\n')
    key = input('print key(word)\n')
    if choice == 'e':
        return vigenere(input_file, output_file, key, 'encrypt')
    elif choice == 'd':
        return vigenere(input_file, output_file, key, 'decrypt')


choice_dict = {'caesar': caesar_work, 'vigenere': vigenere_work}


def start():
    while True:
        choice = input('caesar, vigenere or quit\n')
        if choice == 'quit':
            break
        global choice_dict
        choice_dict[choice]()


start()
