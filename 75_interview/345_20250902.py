class Solution:
    def reverseVowels(self, s: str) -> str:
        word_list = list(s)
        new_list = []
        vowel_list = ['a', 'e', 'i', 'o', 'u']

        for i in range(len(s)):
            if s[i].lower() in vowel_list:
                new_list.append(s[i])

        for j in range(len(word_list)):
            if word_list[j].lower() in vowel_list:
                word_list[j] = new_list.pop()

        print(new_list)
        return ''.join(word_list)

        

        