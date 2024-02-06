def check_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False


print(check_palindrome('потоп'))
print(check_palindrome('привет'))
