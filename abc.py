import math
def BinaryToOctal(binary):
    octal = 0
    decimal = 0
    i = 0
    while (binary != 0):
        decimal = decimal + (binary % 10) * pow(2, i)
        i += 1
        binary = binary // 10
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = decimal // 8
        i = i * 10
    return octal
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
def BinaryToHexadecimal(binary):
    decimal=BinaryToDecimal(binary)
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ''
    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal
def OctaltoBinary(octnum):
    rev = 0
    chk = 0
    while octnum != 0:
        rem = octnum % 10
        if rem > 7:
            chk = 1
            break
        rev = rem + (rev * 10)
        octnum = int(octnum / 10)
    if chk == 0:
        octnum = rev
        binnum = ""
        while octnum != 0:
            rem = octnum % 10
            if rem == 0:
                binnum = binnum + "000"
            elif rem == 1:
                binnum = binnum + "001"
            elif rem == 2:
                binnum = binnum + "010"
            elif rem == 3:
                binnum = binnum + "011"
            elif rem == 4:
                binnum = binnum + "100"
            elif rem == 5:
                binnum = binnum + "101"
            elif rem == 6:
                binnum = binnum + "110"
            elif rem == 7:
                binnum = binnum + "111"
            octnum = int(octnum / 10)
        return binnum
def OctalToDecimal(n):
    decimal = 0
    multiplier = 1
    while(n):
        digit = n % 10
        n = int(n/10)
        decimal += digit * multiplier
        multiplier = multiplier * 8
    return decimal
def OctalToHexadecimal(onum):
    chk = i = dnum = 0
    while onum != 0:
        rem = onum % 10
        if rem > 7:
            chk = 1
            break
        dnum = dnum + (rem * (8 ** i))
        i = i + 1
        onum = int(onum / 10)
    if chk == 0:
        hnum = ""
        while dnum != 0:
            rem = dnum % 16
            if rem < 10:
                rem = rem + 48
            else:
                rem = rem + 55
            rem = chr(rem)
            hnum = hnum + rem
            dnum = int(dnum / 16)
        hnum = hnum[::-1]
        return hnum
def DecimalToBinary(decimal):
    binary = 0
    ctr = 0
    temp = decimal
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    return binary
def DecimalToOctal(decimal):
    octal = 0
    ctr = 0
    temp = decimal
    while (temp > 0):
        octal += ((temp % 8) * (10 ** ctr))
        temp = int(temp / 8)
        ctr += 1
    return octal
def DecimalToHexaDecimal(decimal):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ''
    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    return hexadecimal
def HexaDecimalToBinary(hexdecnum):
    binnum = ""
    hexlen = len(hexdecnum)
    i = 0
    while i < hexlen:
        if hexdecnum[i] == '0':
            binnum = binnum + "0000"
        elif hexdecnum[i] == '1':
            binnum = binnum + "0001"
        elif hexdecnum[i] == '2':
            binnum = binnum + "0010"
        elif hexdecnum[i] == '3':
            binnum = binnum + "0011"
        elif hexdecnum[i] == '4':
            binnum = binnum + "0100"
        elif hexdecnum[i] == '5':
            binnum = binnum + "0101"
        elif hexdecnum[i] == '6':
            binnum = binnum + "0110"
        elif hexdecnum[i] == '7':
            binnum = binnum + "0111"
        elif hexdecnum[i] == '8':
            binnum = binnum + "1000"
        elif hexdecnum[i] == '9':
            binnum = binnum + "1001"
        elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
            binnum = binnum + "1010"
        elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
            binnum = binnum + "1011"
        elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
            binnum = binnum + "1100"
        elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
            binnum = binnum + "1101"
        elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
            binnum = binnum + "1110"
        elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
            binnum = binnum + "1111"
        i = i + 1
    return binnum
def HexaDecimalToOctal(hex):
    value = 0
    decimal = 0
    j = len(hex)
    j -= 1
    for i in range(0, len(hex)):
        if hex[i] >= '0' and hex[i] <= '9':
            value = (int)(hex[i])
        if hex[i] == 'A' or hex[i] == 'a':
            value = 10
        if hex[i] == 'B' or hex[i] == 'b':
            value = 11
        if hex[i] == 'C' or hex[i] == 'c':
            value = 12
        if hex[i] == 'D' or hex[i] == 'd':
            value = 13
        if hex[i] == 'E' or hex[i] == 'e':
            value = 14
        if hex[i] == 'F' or hex[i] == 'f':
            value = 15
        decimal = decimal + (int)(value * math.pow(16, j))
        j -= 1
    sem = 1
    octal = 0
    while (decimal != 0):
        octal = octal + (decimal % 8) * sem
        decimal = decimal // 8
        sem = int(sem * 10)
    return octal
def HexaDecimalToDecimal(hexadecimal):
    hexadecimal=hexadecimal.strip().upper()
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    power = len(hexadecimal) - 1
    for digit in hexadecimal:
        decimal += conversion_table[digit] * 16 ** power
        power -= 1
    return (decimal)
#print(BinaryToOctal(int('11000111001100010110101')))
#print(BinaryToDecimal(int('11000111001100010110101')))
#print(BinaryToHexadecimal(int('0011101000111111110111011101')))
#print(OctaltoBinary(int(123123)))
#print(OctalToDecimal(int(123123)))
#print(OctalToHexadecimal(int(123123)))
#print(DecimalToBinary(int(88343875478)))
#print(DecimalToHexaDecimal(int(88343875478)))
#print(DecimalToOctal(int(88343875478)))
#print(HexaDecimalToDecimal('ABC882CA'))
#print(HexaDecimalToOctal('ABC882CA'))
#print(HexaDecimalToBinary('ABC882CA'))