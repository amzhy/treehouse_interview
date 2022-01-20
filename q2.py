#Q2
def exists(v):
    try:
        v
    except NameError:
        return False;
    return True;

#Q3
def printPascal(n):
    for level in range(1, n+1):
        c=1;
        for i in range(1, level+1):
            print(c, end=" "); 
            c=int(c * (level-i) / i);
        print("");

printPascal(13);
