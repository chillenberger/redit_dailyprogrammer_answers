import math

# date 4/21/22
def lettersum(text):
    return sum(ord(c)-ord('a')+1 for c in text)


if __name__ == "__main__":
    print(lettersum(input()))
