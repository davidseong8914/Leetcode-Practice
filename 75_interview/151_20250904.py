class Solution:
    def reverseWords(self, s: str) -> str:

        word_list = s.split(' ')
        new_word_list = []

        print(word_list)
        for i in reversed(word_list):
            if i != '':
                new_word_list.append(i)
                new_word_list.append(' ')
            else:
                pass
        
        new_word = ''.join(new_word_list)
        new_word = new_word.strip()

        return new_word

        