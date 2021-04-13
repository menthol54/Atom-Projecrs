import random
from indexes import characters
def main():
    letter = ""
    for i in range(1):
        i = random.choice(characters)
        letter += i + letter
        print(letter)
if __name__ == '__main__':
    main()
