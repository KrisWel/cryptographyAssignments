import hashlib
import time


def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


textFirst = input("Input text: ")
text = textFirst.encode()

start = time.time()
md5 = hashlib.md5(text)
hexmd5 = md5.hexdigest()
print("Lenght:", len(hexmd5))
print("Result of md5:", md5.hexdigest())
print("Time of md5:", time.time() - start)

print("")

start = time.time()
sha1 = hashlib.sha1(text)
print("Lenght:", len(sha1.hexdigest()))
print("Result of sha1:", sha1.hexdigest())
print("Time of sha1:", time.time() - start)

print("")

start = time.time()
sha2 = hashlib.sha256(text)
print("Lenght:", len(sha2.hexdigest()))
print("Result of sha2:", sha2.hexdigest())
print("Time of sha2:", time.time() - start)

print("")

start = time.time()
sha3 = hashlib.sha384(text)
print("Lenght:", len(sha3.hexdigest()))
print("Result of sha3:", sha3.hexdigest())
print("Time of sha3:", time.time() - start)

print("")

res = ''.join(format(ord(i), '08b') for i in textFirst)
arr = list(res)
if arr[0] == '0':
    arr[0] = '1'
else:
    arr[0] = '0'
oneBitChanged = ''.join(arr)
oneBitChanged = frombits(oneBitChanged)
oneBitChanged = oneBitChanged.encode()
md5Again = hashlib.md5(oneBitChanged)
md5Again = md5Again.hexdigest()
print(md5Again)

l1 = list(md5Again)
l2 = list(hexmd5)
count = 0
for i in range(len(l1)):
    if l1[i] != l2[i]:
        count += 1
print("Lenght of md5:", len(hexmd5))
print("Bits changed:", count)
# md5 nie jest bezpieczna, tam gdzie wymagana jest odpornosc na kolizja (dwie rozne wiadomosci moga dac ten sam wynik funkcji skrotu)
