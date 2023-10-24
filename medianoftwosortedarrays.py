#4. Median of Two Sorted Arrays
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

class Array():
    def medianofsortedarray(self,nums1,nums2):
        A =nums1
        B = nums2
        total = len(A)+len(B)
        half = total//2
        if(len(A)>len(B)):
            A,B = B,A

        l=0
        r=len(A)-1

        while True:
            i = (l+r)//2
            j = half-i-2
            Aleft = A[i] if i>=0 else float('-infinity')
            Aright = A[i+1] if i+1 < len(A) else float('infinity')
            Bleft = B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if j+1 < len(B) else float('-infinity')

            if(Aleft <= Bright and Bleft <= Aright):
                if(total%2):
                    return(min(Aright,Bright))
                else:
                    return(max(Aleft,Bleft)+min(Aright,Bright))/2
            elif(Aleft>Bright):
                r = i-1
            else:
                l=i+1

a =Array()
print(a.medianofsortedarray([1,2],[3,4]))
