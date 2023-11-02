#238. Product of Array Except Self
#Given an integer array nums, return an array answer such that answer[i] is equal
# to the product of all the elements of nums except nums[i].
#You must write an algorithm that runs in O(n) time and without using the division operation.

class ProductofArray():
    def productexceptself(self,nums):
        res=[1]*len(nums)
        
        prefix=1
        for i in range(0,len(nums)):
            res[i]=prefix
            prefix=prefix*nums[i]

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]

        return(res)

p=ProductofArray()
print(p.productexceptself([1,2,3,4]))


