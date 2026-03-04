
def multi_rec(num1, num2):
    if (num1 == 1):
        return num2
    
    return num2+multi_rec(num1-1, num2)

def soma_rec(num1, num2):
    num1 = num1 + num2
    num2 = 0
    if(num1 == 1):
        return 1
    return 1+soma_rec(num1-1, num2)

def soma_frac_rec(n):
    if(n == 1):
        return 1
    return 1/n + soma_frac_rec(n-1)

def invers_rec(s):
    if (len(s) == 1):
        return s
    return s[len(s)-1] + invers_rec(s[:len(s)-1])

def sequencia_rec(n):
    if(n==1):
        return 1
    elif (n==2):
        return 2
    
    return 2*sequencia_rec(n-1)+3*sequencia_rec(n-2)

def ackerman(m, n):
    if(m == 0):
        return n+1
    if m!=0 and n==0:
        return ackerman(m-1, 1)
    return ackerman(m-1, ackerman(m, n-1))

def soma_e_prod(lst):
    if(len(lst) == 1):
        return lst[0], lst[0]
    
    soma = lst[0] + soma_e_prod(lst[1:])[0]
    prod = lst[0] * soma_e_prod(lst[1:])[1]
    return soma, prod

def palindromo_rec(s):
    if(len(s) == 2):
        return s[0] == s[1]
    elif(len(s) == 1):
        return True
    else:
        if(s[0] != s[len(s)-1]):
            return False
        else:
            s = s[1:len(s)-1]
            return palindromo_rec(s)

#print(palindromo_rec("pedro"))

#print(palindromo_rec("abba"))

def combs(n):
    s = "abcdefghijklmnopqrstuvwxyz"
    inicial = s[:n]
    






