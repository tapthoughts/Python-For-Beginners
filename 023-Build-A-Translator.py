def translate(phrase):
    translation = ""
    for letters in phrase:
        if letters.lower() in "aeiou":
            if letters.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letters
    return translation


print(translate(input("Enter a phrase: ")))