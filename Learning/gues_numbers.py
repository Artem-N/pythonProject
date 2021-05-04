from random import randint
a = randint(0,101)
print("Ти повинен вгадати рандомне число")
print("Якщо відгадка буде далі чи ближче ніж на 10 від мого числа, я скажу холодно або тепло")
print("Якщо відгадка буде далі або ближче від попереднього числа то я скажу холодніше або тепліше")
print("Успіху")
gueses = [0]

while True:
    guess = int(input("Enter your numbrs 0 to 100 "))

    if guess <1 or guess >100:
        print('to much, lets try more: ')
        continue

    if guess == a:
        print(f'You right, you have {len(gueses)} entering')
        break

    gueses.append(guess)

    if gueses[-2]:
        if abs(a-guess) < abs(a-gueses[-2]):
            print("Warmer")
        else:
            print("Colder")
    else:
        if abs(a-guess) <=10:
            print("Warm")
        else:
            print("Cold")
