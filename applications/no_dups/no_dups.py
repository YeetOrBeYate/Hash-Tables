def no_dups(s):
    # Implement me.

    cache = {}

    string = s.split()


    returnString = ""

    for x in string:
        if x not in cache:
            cache[x] = x
            if x != len(string):
                returnString += cache[x] + " "
            else:
                returnString += cache[x]
            

            
    
    return returnString.rstrip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello poop"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))