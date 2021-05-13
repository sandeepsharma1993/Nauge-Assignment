from sys import argv
file = argv[1]


def encode(letter):

    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'

    if letter in lowers:
        return lowers[-1- lowers.find(letter)]

    if letter in uppers:
        return uppers[-1- uppers.find(letter)]

    return letter

output=''
with open(file) as f:

    while(True):
        line = f.readline()
        if not line:
            break

        print(line)

        for letter in line:
            output = output + encode(letter)
output_file='output.txt'
with open(output_file,'w') as o:
    o.write(output)
