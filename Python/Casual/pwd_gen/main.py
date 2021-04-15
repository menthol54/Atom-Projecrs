import random
from indexes import characters
from indexes import symbols

def length():
    user = int(input("Length: "))
    if user > 5:
        pass
    else:
        print('Not working')


def main():
    length()
    letter = ""
    for i in range(1):
        i = random.choice(characters and symbols)
        letter += i
        print(letter)

if __name__ == '__main__':
    main()
