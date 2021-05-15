from sys import argv


def encode(line):
    n = ord('z') + ord('a')
    N = ord('Z') + ord('A')
    atbash=''
    chars  = [] 
    for c in line:
        if c.isalpha() and  c.isupper() :
            chars.append( chr(N - ord(c)))
        elif c.isalpha() and  c.islower():
            chars.append( chr(n - ord(c)))
        else:
            chars.append(c)
    return atbash.join(chars)



if __name__ == '__main__':
    input_file = argv[1]
    result=''
    with open(input_file) as f:
        line = f.readlines()
    
    import  concurrent.futures as cf
    with cf.ThreadPoolExecutor() as executor:
        result = list(executor.map(encode, line))
    
    output_file='output.txt'
    with open(output_file,'w') as o:
        o.writelines(result)
    
