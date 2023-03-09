import sys

file = sys.argv[1]


def no_of_letters(letter):
    with open(sys.argv[1], 'r') as f:
        contents = f.read()
    return contents.count(letter)


count = no_of_letters("e")
print(count)

print(f"The letter 'e' appears {count} times in the file {file}")
