while True:
    n = int(input("Nhap mot so N: "))
    if n <= 1:
        print("Giá trị ko hợp lệ, nhập lại")
        continue
    else:
        i = 0
        for j in range(n+1):
            i += j
        print(i)
        break