class Solution:
    def compress(self, chars: List[str]) -> int:
        # is there a way to do this without a for loop?

        counter = 1

        for i in range(len(chars)):
            if i != 0:
                if chars[i] == chars[i-1]:
                    counter += 1
                    del chars[i]
                else:
                    chars.insert(i,str(counter))
                    counter = 1

        return len(chars)


            

        return len(s)

        