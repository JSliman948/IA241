"""
Lecture 7: While Loops
"""
i=5
while i >=0:
    print(i)
    i = i-1
    
    if i ==3:
        pass
    
    print(i)
#exceptions section
try:
    print(1/0)
except:
    print("error")
    
try:
    print(1+0)
except:
    print("error")