def wordCounter():
    user_input = input("Enter the sentence: ")
    words = user_input.split()
    return len(words)

print(wordCounter())