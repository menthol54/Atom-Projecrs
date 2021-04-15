import random
from indexes import characters
from indexes import symbols
5
def main():
    letter = ""
    for i in range(1):
        i = random.choice(characters and symbols)
        letter += i
        print(letter)




if __name__ == '__main__':
    main()
