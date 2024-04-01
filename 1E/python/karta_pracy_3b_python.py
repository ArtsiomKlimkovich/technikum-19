# zad 1
# for i in range(1, 31):
# 	print(i)

# zad 2
# for i in range(1, 10, 2):
# 	print(i**2)

# zad 3
# for i in range(1000, 9999):
# 	if i % 379 == 0:
# 		print(i)

# zad 4
#for i in range(100, 1000):
#    if i%5==0 and i%6==0 or i%5 != 0 and i%6 != 0 and i%11==0:
#        print(i)

# zad 5
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
# 	input()
# 	sum += i

# print(sum)

# zad 6
# sum = 0
# k = int(input())
# for i in range(2, k*2+1, 2):
# 	sum += i
# print(sum)

# zad 7
# m = int (input())
# sum = 0
# for i in range(11, (m * 2) + 11, 2):
# 	if i < 100:
# 		sum += i
# print(sum)

# zad 8
# w = int (input ("How much you pay: "))
# l = int (input ("How much years: "))
# sum = 0
# cap = w
# for i in range(1, l + 1):
# 	sum = cap * 0.06
# 	cap += sum

# print(round(sum, 2))

# zad 9
# n = int (input())
# a = 0
# sum = 0
# for i in range(n):
# 	a = i * 100 + 21
# 	sum += a

# print(sum)

# zad 10

for i in range (1, 1001):
    if i % 10 == (i ** 0.5) or i % 100 == (i ** 0.5):
        print(i)