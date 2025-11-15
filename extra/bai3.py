x = input("Nhap so nguyen X = ")

if not x.isdigit() or len([ch for ch in x]) == 0:
    print("Invalid input")
    exit(1)

print("Số Chữ số của X:", len(x.strip("")))
print("Chữ số đầu tiên của X:", x.strip("")[0])