class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = 0
        new_word_list = []

        while (i < min(len(word1), len(word2))):
            new_word_list.append(word1[i])
            new_word_list.append(word2[i])
            i+=1
        
        if (len(word1) > len(word2)):
            new_word_list.append(word1[len(word2):])
        else:
            new_word_list.append(word2[len(word1):])

        
        return ''.join(new_word_list)



        