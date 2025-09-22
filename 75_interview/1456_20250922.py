class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        s_sep = list(s)
        max_count = 0

        first_set = s_sep[0:k]
        for let in first_set:
            if let in vowel_list:
                max_count += 1

        current_count = max_count 

        for i in range(k, len(s_sep)):
            if s_sep[i-k] in vowel_list:
                current_count -= 1
            if s_sep[i] in vowel_list:
                current_count += 1
            
            max_count = max(current_count, max_count)

            if max_count == k:
                return max_count

        return max_count

        
        