# binary 2's complement 

def TwosComplement(binary):
    n = len(binary)
 
    i = n - 1
    while(i >= 0):
        if (binary[i] == '1'):
            break
 
        i -= 1
 
    if (i == -1):
        return '1'+binary

    k = i - 1
    while(k >= 0):
         
        if (binary[k] == '1'):
            binary = list(binary)
            binary[k] = '0'
            binary = ''.join(binary)
        else:
            binary = list(binary)
            binary[k] = '1'
            binary = ''.join(binary)
 
        k -= 1
    return binary
 
if __name__ == '__main__':
    decimal=int(input("input your decimal: "))
    binary=str(bin(decimal)[2:])
    final=TwosComplement(binary)
    print(f"1"+final)
 