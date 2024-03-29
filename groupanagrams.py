#49. Group Anagrams
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#Typically using all the original letters exactly once.

from collections import defaultdict

class Groupanagram():
    def anagramgroup(self,strs):
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for i in range(0,len(s)):
                count[ord(s[i])-ord('a')]=1+ count[ord(s[i])-ord('a')]
            res[tuple(count)].append(s)
        return res.values()

g=Groupanagram()
print(g.anagramgroup(["eat","tea","tan","ate","nat","bat"]))

