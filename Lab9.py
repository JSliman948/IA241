"""
Lab 9: Class
"""
#3.1
class my_stat:
    def cal_sigma (self, m, n):
        result = 0
        for i in range (n, m+1):
            result = result + i
        return result
    def cal_pi(self, m, n):
        result = 1 
        for i in range (n, m+1):
            result = result * i
        return result
    def cal_f(self, m):
        if m == 0:
            return 1
        else:
            return m * self.cal_f(m-1)
    def cal_p(self, m, n):
        return self.cal_f(m)/self.cal_f(m-n)
#3.2
my_cal = my_stat()
print(my_cal.cal_sigma(5, 3))

my_pi = my_stat()
print(my_pi.cal_pi(5,3))

my_factorial = my_stat()
print(my_factorial.cal_f(5))

my_permutation = my_stat()
print(my_permutation.cal_p(5,2))