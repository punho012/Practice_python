def palindrome():
    word = input("Enter a word: ")
    sp = list(word)
    sp.reverse()
    together = "".join(sp)
    if together == word:
        return "this is a palindrome"
    return "This is not  palindrome"
    
    

print(palindrome())
