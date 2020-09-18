'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if not word:
        return 0
    if word.islower():
        return word.count('th')
    else:
        return count_th(word.lower())
