def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def nwd(a, b): return nwd(b, a % b) if b else a


p = 1019
q = 1021
n = p * q
phi = (p - 1) * (q - 1)

e = 0
for i in range(2, phi):
    if isprime(i) and nwd(i, phi) == 1:
        e = i
        break
print("e:", e)
d = 0
for i in range(2, phi):
    d = i
    if (e * d - 1) % phi == 0:
        break
print("d:", d)

# szyfrowanie
message = "Lorem ipsum dolor sit amet, consectetur cras amet."
cipher = []
for i in message:
    tempM = ord(i)
    cipher.append((tempM ** e) % n)
print(cipher)

# deszyfrowanie
deCipher = []
for i in cipher:
    tempM = chr((i ** d) % n)
    print(tempM)
    # deCipher.append(tempM)
# print(deCipher)
