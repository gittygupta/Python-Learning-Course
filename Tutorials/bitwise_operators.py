
# ------ Binary AND ------

a = 50      # 110010
b = 25      # 011001
c = a & b   # 010000 = 16
# '&' is a binary operator

print(c)

# ------ Binary RIGHT SHIFT ------

x = 240     # 11110000
y = x >> 2  # 00111100 = 60
# Every bit shifted 2 places to the right

print(y)

# ------ Binary LEFT SHIFT ------
z = x << 4  # 00001111
print(z)

# ------ Binary OR ------

d = a | b   # 111111
print(d)

# ------ Binary compliment ------

e = ~x
print(e)

# ------ Binary XOR ------

f = a ^ b    #101011
print(f)