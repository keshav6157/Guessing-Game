import random

num = random.randint(1, 100)
print('WELCOME TO GUESSING GAME!')

guesses = [0]


while True:
    guess = int(input('enter the guess:'))
    if guess < 1 or guess > 100:
        print('out of limit!')
        continue

    if guess == num:
        print(f'congo u got correct guess in {len(guesses)} guesses!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if (abs(num-guess)) < (abs(num-guesses[-2])):
            print('warmer')
        else:
            print('colder')

    else:
        if (abs(num-guess) <= 10):
            print('warm')
        else:
            print('cold')