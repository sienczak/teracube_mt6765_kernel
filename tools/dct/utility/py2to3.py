def atoi(s: str) -> int:
    resultant = 0
    for i in range(len(s)):
        resultant = resultant * 10 + (ord(s[i]) - ord('0'))        #It is ASCII substraction 
    return resultant


def cmp(a: any, b: any) -> any:
    return (a > b) - (a < b)

