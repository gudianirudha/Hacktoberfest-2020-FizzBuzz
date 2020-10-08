#Author: Chidu2000
# A lengthy python code to implement fizzbuzz using function call
# object oriented approach

class Solution(object):

   # function creation 
   def fizzBuzz(self, n):
      """
      :type n: int
      :rtype: List[str]
      """
      
      # creating a result array and appending the results 
      result = [] 
      
      # looping over the values
      for i in range(1,n+1):
         if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
         elif i %3==0:
            result.append("Fizz")
         elif i% 5 == 0:
            result.append("Buzz")
         else:
            result.append(str(i))
      return result
      
   # function call   
ob1 = Solution()
print(ob1.fizzBuzz(30))
