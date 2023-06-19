#8. String to Integer (atoi)
#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#The algorithm for myAtoi(string s) is as follows:
#Read in and ignore any leading whitespace.
#Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
# This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
#Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
#Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
#If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
# Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
#Return the integer as the final result.
#s = '  -2458lsj'

class Stringtointeger():
    def myatoi(self,s):
        s=s.lstrip()
        if(not s):
            return(0)
        sign=1
        i=0
        if(s[i]=='+'):
            i=1
        elif(s[i]=='-'):
            sign=-1
            i=1
        print(sign)
        result=0
        while(i<len(s)):
            if(s[i].isdigit()):
                result=result*10 + int(s[i])
                i = i + 1
            else:
                break

        result=result*sign
        if(result> (2**31)-1):
            return((2**31)-1)
        elif(result<(-2**31)):
            return(-2**31)
        else:
            return(result)
s=Stringtointeger()
print(s.myatoi('   -896yur42'))


