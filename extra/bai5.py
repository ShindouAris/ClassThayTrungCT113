diem30 = float(input("Nhap diem qua trinh ") or 0)
diem30_gk = float(input("Nhap diem giua ki ") or 0)
diem40_ck = float(input("Nhap diem cuoi ki ") or 0)

if diem30 == 0 or diem30_gk == 0 or diem40_ck == 0:
    print("Bạn đã rớt (Điểm liệt)")
    exit(0)

diemTB = (diem30 * 0.3) + (diem30_gk * 0.3) + (diem40_ck * 0.4)

if diemTB >= 4:
    print("Bạn đã đậu, điểm của bạn là", diemTB)
else:
    print("Bạn rớt thảm hại luôn, điểm của bạn là", diemTB)