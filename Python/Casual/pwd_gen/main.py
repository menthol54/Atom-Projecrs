import random
from indexes import characters

def main():
    for i in range(0, 36):
        i = random.choice(characters)
        print(i)
if __name__ == '__name__':
    main()
