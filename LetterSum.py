
# date 4/21/22
# https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/
# This program finds the value of the positional value of the letters of the word
# submitted. for example ''=0, 'a'=1, 'b'=2... therfore hello = 52

def lettersum(text):
    return sum(ord(c)-ord('a')+1 for c in text)


if __name__ == '__main__':
    print(lettersum('hello'))
    print(lettersum('microspectrophotometries'))
