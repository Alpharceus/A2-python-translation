r=""
while r != 'n':
    list = input('Enter a list of numbers seperated by commas:')
    a = list.split(',')
    n = int(len(a))


    pos = 0
    T = 0
    i = 1
    while i == 1:
        s = 1
        j = 0
        num = []
        while s > 0:
            j = j + 1
            s = 0
            while pos < n - 1:
                if int(a[pos]) > int(a[pos + 1]):
                    s = s + 1
                    x = int(a[pos])
                    y = int(a[pos + 1])
                    a[pos] = y
                    a[pos + 1] = x
                pos = pos + 1
            T =  T + 1
            print('pass',T,':',a)
            pos = 0
            if T == n - 1:
                s = 0
            num.append(a[n - j])
        if s == 0:
            i = 0
    print('total number of passes:', T)
    r=input("Do you want to sort another list? (y/n)")

