def swap_case(s):
    new=[ch.lower() if ch.isupper() else ch.upper() for ch in s]
    new=''.join(new)
    return new
    

     

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
