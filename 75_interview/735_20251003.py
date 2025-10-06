class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survived_asteroids = []
        for i in range(len(asteroids)):
            if not(survived_asteroids) or not(survived_asteroids[-1] > 0 and asteroids[i] < 0):
                survived_asteroids.append(asteroids[i])
            else:
                while survived_asteroids and abs(asteroids[i]) > survived_asteroids[-1] and survived_asteroids[-1] > 0:
                    survived_asteroids.pop()

                if not(survived_asteroids) or survived_asteroids[-1] < 0:
                    survived_asteroids.append(asteroids[i])
                elif survived_asteroids[-1] == abs(asteroids[i]):
                    survived_asteroids.pop()
                else:
                    pass

                


        return survived_asteroids


        