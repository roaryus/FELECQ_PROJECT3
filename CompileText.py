filename = ['8P-1.txt', '8P-2.txt', '8P-3.txt', '8P-4.txt', '8P-5.txt']
with open('8P.txt', 'w') as outfile:
    for fname in filename:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)