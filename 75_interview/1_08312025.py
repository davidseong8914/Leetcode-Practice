class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        short_word = word1 if len(word1) < len(word2) else word2
        long_word = word1 if len(word1) > len(word2) else word2
        new_word_list = []

        if len(word1) == len(word2):
            for i in range(len(word1)):
                new_word_list.append(word1[i])
                new_word_list.append(word2[i])
        else:
            for i in range(len(short_word)):
                new_word_list.append(word1[i])
                new_word_list.append(word2[i])
            
            new_word_list.append(long_word[len(short_word):])

        
        return ''.join(new_word_list)



        