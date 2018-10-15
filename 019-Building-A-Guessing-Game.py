word = "abstract"
count = 0
guess = ""
limit = 2
lose = False


print("Guess the Word! You'll get three chances")
while guess != word and not lose:
    if count <= limit:
        guess = input("A word so random, you almost know nothing about it:")
        count += 1
        if guess != word:
            print("Duh! TRY AGAIN")

    else:
        lose = True
        print("You Lose faggot!")


if not lose:
    print("You Win kiddo!")