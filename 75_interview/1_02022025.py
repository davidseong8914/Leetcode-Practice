#1768. Merge Strings Alternately
#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = 0
        merged = []
        while i < (min(len(word1), len(word2))):
            merged.append(word1[i])
            merged.append(word2[i])
            i = i+1

        # optimize by making it not have to compare everytime
        while i < (max(len(word1)), max(len(word2))):
            if (word1.length() > word2.length()):
                merged.append(word1[i])
            else:
                merged.append(word2[i])

        rtr_str = ''.join(merged)
        return rtr_str

            
                   

        