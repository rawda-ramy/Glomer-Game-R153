with open('jk.txt', 'r') as f:
    for line in f.readlines():
        data = line.rsplit()
        j, k = data.split('=')
        print(j + 'for' + k)

