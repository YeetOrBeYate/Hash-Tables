import re


def word_count(s):
    cache = {}
    
    # Implement me.

    #must use toLower
    #

    yeet = s.split()

    foot = []

    for x in yeet:
        y = re.sub('[!@#$,".:;+=\/|{}()*^&-]', '', x)
        y = y.replace("[]", "")
        y = y.replace("\\", "")
        y = y.lower()
        foot.append(y)

    for z in foot:
        if z not in cache:
            cache[z] = 1
        else:
            cache[z] +=1

    empty = ''
    if empty in cache:
        del cache[empty]

    return cache


if __name__ == "__main__":
    print(word_count("[]"))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))