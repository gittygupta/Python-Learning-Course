from struct import *

# Store as bytes data

# Struct is something that converts something that humans can read to 1's and 0's, and vice versa

# Converting into byte format:
packed_data = pack('iif', 6, 19 , 4.73)      # It takes in the format of each number followed by the numbers/values
                                            # 'iif' means 2 int and 1 float value. If we enter 5 int we need to enter 'iiiii'

print(packed_data)      # It prints it out in byte format

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))  # It prints the amount of memory needed to store the given data

# Converting bytes to readable format:

unpacked_data = unpack('iif', packed_data)
print(unpacked_data)
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))        # It gives the same result
