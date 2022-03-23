"""
Lecture 8: Functions
"""
def Morrocco(a,b=0):
    print(a)
    print(b)
    
    result = a + b 
    return result
    
print(Morrocco(b=1, a=2))
#I don't really know why I named my function Morrocco. It seemed more fun than my_function

#Exercise 1: Calculate Absolute Values
def cal_abs(a):
    if type(a) is str:
        return ("Wrong data type Buckaroo")
    elif a >= 0:
        return a
    else:
        return -a
        
print(cal_abs(1))

#Exercise 2: Caclulating Sigma and Pi
def cal_sigma(m,n):
    result = 0
    for i in range(n,m+1):
        
        result = result + i
    return result
print(cal_sigma(5,3))

def cal_pi(m,n):
    result = 1
    for i in range(n,m+1):
        result = result*i
    return result
print(cal_pi(5,3))
  
#Exercise 3: Calculating a Factorial and a Permutation
def cal_f(m):
    if m == 0:
        return 1
    else:
        return m*cal_f(m-1)
print(cal_f(3))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
print(cal_p(5,3))