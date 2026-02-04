class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        first = False
        
        for i in range(len(word)):
            if i == 0 and word[i] == word[i].upper():
                first = True
                count += 1
            elif word[i] == word[i].upper():
                count += 1
            else:
                pass

        if first == True and count == 1:
            return True
        elif count == len(word):
            return True
        elif count == 0:
            return True
        else:
            return False

        
            
# could have been 
# return word.isupper() or word.istitle or word.islower() ...lol