def palindrome_trivial(s):
    if s == s[::-1]:
        return True
    else:
        return False

def palindrome_iterative(s):
    i = 0
    while i <= len(s) / 2:
        if s[i] != s[-i - 1]:
            return False
        i += 1
    return True

def palindrome_recursive(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome_recursive(s[1:-1])
        else:
            return False


def main():
    s = input("Type a word: ")
    s = s.lower()
    s = s.strip()
    s = s.replace(" ", "")
    print("{0} {1}: {2}".format(s, "is palindrome", palindrome_trivial(s)))
    print("{0} {1}: {2}".format(s, "is palindrome", palindrome_iterative(s)))
    print("{0} {1}: {2}".format(s, "is palindrome", palindrome_recursive(s)))

if __name__ == "__main__":
    main()