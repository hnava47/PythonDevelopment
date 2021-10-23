def palindrome(word):
    newWord = word[::-1]

    if newWord.lower() == word.lower():
        return "Word is a palindrome"
    else:
        return "Word is not a palindrome"

w = "noon"
palindrome(w)
