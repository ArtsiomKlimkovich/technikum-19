# zad 1
def printBinarySequence (n, prefix="", lastDigit=0, OneInRow=0):
    if n == 0:
        print (prefix)
        return 1
    
    total = 0
    
    for digit in range (2):
        if digit == 1 and lastDigit == 1:
            continue
        if digit == 1:
            OneInRow += 1
        else:
            OneInRow = 0
        total += printBinarySequence(n-1, prefix + str(digit),digit, OneInRow)
    return total
n = int(input("input bin num: "))
print (f"dla {n} ilosc ciagow jest to {printBinarySequence(n)}")

def generate_binary_palindromes(length):
    palindromes = []
    for i in range(2 ** ((length + 1) // 2)):
        palindrome = bin(i)[2:]
        palindrome = '0' * ((length + 1) // 2 - len(palindrome)) + palindrome
        palindrome += palindrome[:-1][::-1]  # Dodajemy odwroconą część bez ostatniego elementu, aby uniknąć podwójnego dodawania dla liczb o parzystej długości
        palindromes.append(palindrome)
    return palindromes

# zad 2
palindromes = generate_binary_palindromes(10)
for palindrome in palindromes:
    print(palindrome)
