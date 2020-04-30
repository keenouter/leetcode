import math
class Solution:
    def countPrimes(self, n: int) -> int:
        sum=0
        for i in range(1,n):
            if self.isPrime(i):
                sum+=1
        return sum
    
    def isPrime(self,n):
        if n<=3:
            return n>1
        
        if n%6!=1 and n%6!=5:
            return False
        sqrt = (int) (math.sqrt(n))
        for i in range(5,sqrt+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
        # div_num=[]
        # for i in range(1,n):          
        #     if n%i==0:
        #         div_num.append(i)
        #     if len(div_num)>=2:
        #         return False

        # if  len(div_num)==1:
        #     return True


print(Solution().countPrimes(10))