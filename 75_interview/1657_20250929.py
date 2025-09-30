class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1_dict = {}
        word2_dict = {}

        for let in word1:
            if let not in word1_dict:
                word1_dict[let] = 1
            else:
                word1_dict[let] += 1

        for let in word2:
            if let not in word2_dict:
                word2_dict[let] = 1
            else:
                word2_dict[let] += 1

        if set(word1_dict.keys()) != set(word2_dict.keys()):
            return False

        if sorted(word1_dict.values()) != sorted(word2_dict.values()):
            return False

        return True