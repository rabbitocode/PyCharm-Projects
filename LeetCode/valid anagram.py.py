

s = "aacc"
t = "ccac"



def isAnagram(self, s, t):
    hashlista = set()
    hashlista_2 = set()

    list = []
    list2 = []
    for x in s:
        hashlista.add(x)
        list.append(x)
    for x in t:
        hashlista_2.add(x)
        list2.append(x)

    list.sort()
    list2.sort()




    if list != list2:
        return False
    elif hashlista == hashlista_2:
        print("True")
        return True
    else:
        print("False")
        return False

isAnagram(0,s,t)





# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?













