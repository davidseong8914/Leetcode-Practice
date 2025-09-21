class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        s_sep = list(s)
        max_vowel_count = 0

        for i in range(k, len(s)+1):
            sub_set = s_sep[i-k: i]
            cvc = 0
            for let in sub_set:
                if let in vowel_list:
                    cvc += 1
            
            if cvc > max_vowel_count:
                max_vowel_count = cvc

        return max_vowel_count

        
        