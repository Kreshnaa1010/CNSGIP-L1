def is_palindrome(s):
   
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
   
    return cleaned == cleaned[::-1]

def main():
    print("Palindrome Checker")
    print("==================")
    print("This program checks if a given string is a palindrome.")
    print("A palindrome reads the same forwards and backwards (ignoring spaces, punctuation, and capitalization).")
    print()

    user_input = input("Enter a string to check: ")
    
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()
