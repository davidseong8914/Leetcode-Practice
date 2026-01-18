# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = False

        def bfs(left, right):
            target = left + ((right - left) // 2)

            num = guess(target)
            if num == 0:
                return target, left, right, True
            elif num == 1:
                #lower than the number
                left = target + 1
            elif num == -1:
                right = target
            
            return target, left, right, False

        left, right = 0, n
        target = -1

        while left <= right:
            target, left, right, answer = bfs(left, right)
            if answer == True:
                return target


        return target
        