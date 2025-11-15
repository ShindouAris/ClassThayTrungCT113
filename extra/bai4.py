x = input("Nhap X co 4 chu so: ")

if not x.isdigit() and len([ch for ch in x]) == 0:
    print("Đầu vào không hợp lệ")

print(f"Tổng các chữ số có trong X: {sum([int(ch) for ch in x])}")