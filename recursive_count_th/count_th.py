'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # Base line:
    if not word:
        return 0
    i = 0
    # slice the word and check the 1st 2 letters, then next ...:
    if word[i:2] == 'th':
        return 1 + count_th(word[i+1:])
    else:
        return count_th(word[i+1:])
