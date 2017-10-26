# listManager.py

def string2List(delimiter, s):
    """Take a delimited string and return a list"""
    L = s.split(delimiter)
    return L

def uniqueList(L):
    """Get unique entries"""
    # Python Set data types hold only unique entries
    # S collects unique entries in L
    S = set(L)
    # Copy S back to L
    U = []
    for i in S:
        U.append(i)
    return U

def list2String(delimiter, L):
    """Take a list and return a delimited string"""
    # Use list comprehension to cast each element to string,
    # because join fails for non-string elements.
    stringL = [str(i) for i in L]

    # Join the string elements of stringL
    s = delimiter.join(stringL)
    return s

if __name__ == "__main__": 
    import sys 
    print string2List(sys.argv[2], sys.argv[1])