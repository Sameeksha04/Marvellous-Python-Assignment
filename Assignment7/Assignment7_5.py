def palindrome(str):
    left = 0
    a=len(str)
    right = a - 1

    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    print("Enter a string: ")
    text= input()
    result = palindrome(text)

    if (result==True):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")

if __name__ =="__main__":
    main()

