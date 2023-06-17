#Rotate String
#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

class Rotatestring():
    def rotatestr(self,s,goal):
        return(len(s)==len(goal) and (goal in s+s))

r = Rotatestring()
print(r.rotatestr('abcde','deabc'))