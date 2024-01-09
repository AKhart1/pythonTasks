def palindromeCheker():
    string = input("Enter a string : ")
    clean_text = ''
    for char in string:
        if char.isalnum():
            clean_text += char.lower()

    return clean_text == clean_text[::-1]

print(palindromeCheker())