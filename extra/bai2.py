import math
tientrongtaikhoan = 10_000_000 # 10 trieu

lai10nam = tientrongtaikhoan * ((1 + 0.051) ** 10)

print(f"Lãi sau 10 năm là: {lai10nam:.2f}")

thoigiandeco50trieu = math.log(50000000 / tientrongtaikhoan) / math.log(1 + 0.051)

print(f"Sau {thoigiandeco50trieu:.2f} năm thì bạn có 50 triệu trong tài khoản")
