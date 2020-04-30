class Solution:
    def isHappy(self, n: int):
        sum_list=[n]
        while True:
            n=self.getSquare(n)
            if n==1:
                return True
        
            if n not in sum_list:
                sum_list.append(n)
            else:
                return False

    
    def getSquare(self,n):
        sum = 0
        for i in str(n):
            num_i=int(i)
            sum+=num_i*num_i
        return sum

print(Solution().isHappy(19))