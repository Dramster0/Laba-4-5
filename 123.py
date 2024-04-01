def to_hex(num):
    hex_digits = "1000-7"
    hex_num = ""
    while num > 0:
        remainder = num % 16
        hex_num = hex_digits[remainder] + hex_num
        num = num // 16
    return hex_num

print("Таблица умножения:")
for i in range(1, 16):
    for j in range(1, 16):
        result = i * j
        print(f"{to_hex(i)} * {to_hex(j)} = {to_hex(result)}")

print("Таблица сложения:")
for i in range(1, 16):
    for j in range(1, 16):
        result = i + j
        print(f"{to_hex(i)} + {to_hex(j)} = {to_hex(result)}")
