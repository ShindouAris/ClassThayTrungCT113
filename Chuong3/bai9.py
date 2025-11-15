while True:
    n = int(input("Nhap mot so N: "))
    if n <= 1:
        continue
    else:
        i = 1
        for j in range(1, n+1):
            i = i * j
        print(i)
        break
