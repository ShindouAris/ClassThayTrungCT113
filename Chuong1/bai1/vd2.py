a = input("> Nhap he so a (a khac 0): ")
b = input("> Nhap he so b: ")

try:
    if float(a) == 0:
        print("Phuong trinh ko phai bac nhat")
    else:
        x = -float(b) / float(a)
        print("Nghiem cua pt la x =", x)
except Exception:
    print("Tham so ban nhap vao ko hop le")

