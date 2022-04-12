import random


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def binaryToDecimal(n):
    return int(n, 2)


p = 1000003
q = 4000039
n = p * q
bitsArray = []
x = random.randint(1, n - 1)

xi = x
temp = pow(xi, 2) % n
while len(bitsArray) <= 20000:
    temp = pow(xi, 2) % n
    xi = temp
    if temp % 2 == 0:
        bitsArray.append('0')
    else:
        bitsArray.append('1')


print("L(1): ", bitsArray.count('1'))
print("L(0): ", bitsArray.count('0'))

print("")

allBits = "".join(bitsArray)


l_1 = []
l_0 = []
temp1 = 0
temp0 = 0
for j in range(0, 20000): 
    if allBits[j] == '0':
        temp0 += 1
        if temp1 != 0:
            l_1.append(temp1)
            temp1 = 0
    elif allBits[j] == '1':
        temp1 += 1
        if temp0 != 0:
            l_0.append(temp0)
            temp0 = 0


sum1 = 0
sum0 = 0
for i in range(1, 26):
    if i >= 6:
        sum0 += l_0.count(i)
    else:
        print("l_0_", i, ":", l_0.count(i))
print("l_0_6+: ", sum0)
for i in range(1, 26):
    if i >= 6:
        sum1 += l_1.count(i)
    else:
        print("l_1_", i, ":", l_1.count(i))
print("l_1_6+: ", sum1)
print("")

l1 = 0
l0 = 0
for i in range(25, 10000):
  l0 += allBits.count('1' + '0' * i + '1')
  l1 += allBits.count('0' + '1' * i + '0')

print("l_1_26+: ", l1)
print("l_0_26+: ", l0)
print("")

i = 0
j = 4
fourBits = []
while j < 20000:
    fourBits.append(allBits[i:j])
    i += 4
    j += 4

decArray = []
for i in fourBits:
    decArray.append(binaryToDecimal(i))


freqDec = []
sum = 0
for i in range(0, 16):
    freqDec.append(decArray.count(i))
    print(i, ":", freqDec[i])
    sum += pow(freqDec[i], 2)

sum = sum * 16/5000
sum = sum - 5000
print("")
print("X: ", sum)