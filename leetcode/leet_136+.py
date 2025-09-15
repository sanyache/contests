def single_number(nums):
   ans = 0
   for num in nums:
       ans ^= num

   return ans   

nums = [4,1,2,1,2]
print(single_number(nums))