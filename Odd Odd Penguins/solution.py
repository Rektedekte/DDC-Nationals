def valid_parity(str_byte):
    return sum(int(bit) for bit in str_byte[:-1]) & 1 != int(str_byte[-1])


with open("defence.txt", "r") as f:
    str_bytes = f.read().split(",")

txt_out = ""

for str_byte in str_bytes:
    if valid_parity(str_byte):
        txt_out += chr(int(str_byte[:-1], base=2))

print(txt_out)
