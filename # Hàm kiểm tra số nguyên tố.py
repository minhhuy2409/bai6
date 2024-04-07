#bài 1
# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra một số nguyên có phải là số nguyên tố không
num = int(input("Nhập một số nguyên: "))
if is_prime(num):
    print(num, "là số nguyên tố")
else:
    print(num, "không là số nguyên tố")

# Đếm số lượng số nguyên tố từ 1 đến n
n = int(input("Nhập số nguyên n: "))
count = 0
for i in range(1, n + 1):
    if is_prime(i):
        count += 1
print("Số lượng số nguyên tố từ 1 đến", n, "là", count)
