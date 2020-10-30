if __name__ == '__main__':
    s = input()
    counts = [0]*26
    # mapping = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
    #  'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 
    #  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    for i in s:
        counts[ord(i)-ord('A')] += 1 
    n = ord('A')
    c = 0
    odd = ''
    for i in range(26):
        if counts[i]%2:
            c += 1
            odd = chr(n + i)*counts[i]
    if c > 1:
        print("NO SOLUTION")
    else:
        s1 = ""
        for i in range(26):
            if counts[i]%2 == 0:
                s1 += chr(n + i)*(counts[i]//2)
        print(s1, end ="")
        print(odd, end ="")
        print(s1[::-1])