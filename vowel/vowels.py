import pathlib
import sys

vowels = set('aeiou')


def is_vowel(char):
    return char in vowels


def is_vowel_line(line):
    if line is None:
        return False
    line_vowel_set = set({})
    for char in line:
        if is_vowel(char):
            line_vowel_set.add(char)
    return len(vowels) == len(line_vowel_set)


def print_file_vowels(filename):
    if not pathlib.Path(filename).exists():
        raise FileNotFoundError
    file = open(filename)
    for line in file:
        if is_vowel_line(line):
            print(line)
    file.close()


def main(filename):
    print_file_vowels(filename)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("please provide file name to print vowel lines")
    else:
        main(sys.argv[1])
