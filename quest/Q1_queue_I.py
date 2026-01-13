class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while students:
            if sandwiches[0] not in students:
                return len(sandwiches)
            else:
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    students.append(students[0])
                    students.pop(0)
        
        return 0


        