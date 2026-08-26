class Solution(object):
    def countStudents(self, students, sandwiches):
        n = 0
        while sandwiches:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                n=0
            else:
                student = students.pop(0)
                students.append(student)
                n += 1
            if n == len(students):
                break 
        return len(students)

        