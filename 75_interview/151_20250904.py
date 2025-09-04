class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        return ' '.join(reversed(word_list))

            