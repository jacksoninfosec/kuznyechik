# Kuznyechik Block Cipher

pi = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 
     233, 119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 
     249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 
     5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 
     235, 52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 
     181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 
     21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177,
     50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 
     223, 245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 
     224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 
     167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 
     173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 
     7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 
     225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97,
	 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 
	 89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182]

pi_inv = [165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145, 
         100, 3, 87, 90, 28, 96, 7, 24, 33, 114, 168, 209, 41, 198, 164, 63, 
         224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229, 66, 228, 21, 183, 
         200, 6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213, 
         195, 175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47, 
         155, 67, 239, 217, 121, 182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 
         162, 223, 166, 254, 172, 34, 249, 226, 74, 188, 53, 202, 238, 120, 5, 107, 
         81, 225, 89, 163, 242, 113, 86, 17, 106, 137, 148, 101, 140, 187, 119, 60, 
         123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 
         219, 105, 179, 20, 149, 190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 
         55, 97, 75, 185, 227, 186, 241, 160, 133, 131, 218, 71, 197, 176, 51, 250,
         150, 111, 110, 194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125, 236, 88, 
         247, 31, 251, 124, 9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 
         235, 248, 243, 62, 61, 189, 138, 136, 221, 205, 11, 19, 152, 2, 147, 128, 
         144, 208, 36, 52, 203, 237, 244, 206, 153, 16, 68, 64, 146, 58, 1, 38, 
         18, 26, 72, 104, 245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116] 


# The input x and the output y have 128-bits
def S(x):
	y = 0
	for i in reversed(range(16)):
		y <<= 8
		y ^= pi[(x >> (8 * i)) & 0xff]
	return y


# The input x and the output y have 128-bits
def S_inv(x):
	y = 0
	for i in reversed(range(16)):
		y <<= 8
		y ^= pi_inv[(x >> (8 * i)) & 0xff]
	return y


# x and y are nonnegative integers 
# Their associated binary polynomials are multiplied. 
# The associated integer to this product is returned. 
def multiply_ints_as_polynomials(x, y):
	if x == 0 or y == 0:
		return 0
	z = 0
	while x != 0:
		if x & 1 == 1:
			z ^= y
		y <<= 1
		x >>= 1
	return z


# Returns the number of bits that are used 
# to store the non-negative integer x.
def number_bits(x):
	if x == 0:
		return 0  
	nb = 0
	while x != 0:
		nb += 1
		x >>= 1
	return nb


# x is a nonnegative integer
# m is a positive integer
def mod_int_as_polynomial(x, m):
	nbm = number_bits(m)
	while True:
		nbx = number_bits(x) 
		if nbx < nbm:
			return x
		mshift = m << (nbx - nbm)
		x ^= mshift


# x,y are 8-bits
# The output value is 8-bits
def kuznyechik_multiplication(x, y):
	z = multiply_ints_as_polynomials(x, y)
	m = int('111000011', 2)
	return mod_int_as_polynomial(z, m)


# The input x is 128-bits (considered as a vector of sixteen bytes)
# The return value is 8-bits
def kuznyechik_linear_functional(x):
	C = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1] 
	y = 0
	while x != 0:
		y ^= kuznyechik_multiplication(x & 0xff, C.pop())
		x >>= 8
	return y


# The input value x and the output value is 128-bits
def R(x):
	a = kuznyechik_linear_functional(x)
	return (a << 8 * 15) ^ (x >> 8)


# The input value x and the output value are 128-bits
def R_inv(x):
	a = x >> 15 * 8
	x = (x << 8) & (2 ** 128 - 1)
	b = kuznyechik_linear_functional(x ^ a)
	return x ^ b


# The input value x and the output value is 128-bits
# This function is the composition of R sixteen times
def L(x):
	for _ in range(16):
		x = R(x)
	return x


# The input value x and the output value are 128-bits
def L_inv(x):
	for _ in range(16):
		x = R_inv(x)
	return x


# k is 256-bits
# The key schedule algorithm returns 10 keys of 128-bits each
def kuznyechik_key_schedule(k):
	keys = [] 
	a = k >> 128
	b = k & (2 ** 128 - 1)
	keys.append(a)
	keys.append(b)
	for i in range(4):
		for j in range(8):
			c = L(8 * i + j + 1)
			(a, b) = (L(S(a ^ c)) ^ b, a) 
		keys.append(a)
		keys.append(b)
	return keys


# The plaintext x is 128-bits
# The key k is 256-bits 
def kuznyechik_encrypt(x, k):
	keys = kuznyechik_key_schedule(k)
	for round in range(9):
			x = L(S(x ^ keys[round]))
	return x ^ keys[-1]


# The ciphertext x is 128-bits
# The key k is 256-bits 
def kuznyechik_decrypt(x, k):
	keys = kuznyechik_key_schedule(k)
	keys.reverse()
	for round in range(9):
			x = S_inv(L_inv(x ^ keys[round]))
	return x ^ keys[-1]




PT = int('1122334455667700ffeeddccbbaa9988', 16)
k = int('8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef', 16)

CT = kuznyechik_encrypt(PT, k)

DT = kuznyechik_decrypt(CT, k)

print(PT == DT)




