a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))

print(f"Tổng: {a+b}")

print(f"Hiệu: {a-b}")

print(f"Tích: {a*b}")

if b == 0:
    print("Không thể chia cho 0")
else:
    print(f"Thương: {a/b}")
    print(f"Chia dư: {a%b}")
    print(f"Chia Nguyên: {a//b}")

