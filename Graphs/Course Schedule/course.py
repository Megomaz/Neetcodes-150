# Not mine
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # Store all courses along the current DFS path
        visited = set()

        def dfs(course):
            # If the course is already in the current path, we have a cycle
            if course in visited:
                return False
            
            # If there are no prerequisites for this course, it’s already processed
            if preMap[course] == []:
                return True
            
            # Mark the course as visited for the current path
            visited.add(course)

            # Recursively visit all prerequisites for this course
            for pre in preMap[course]:
                if not dfs(pre):
                    return False  # Cycle detected in one of the prerequisites

            # After visiting all prerequisites, remove the course from the current path
            visited.remove(course)

            # Mark this course as fully processed by clearing its prerequisites
            preMap[course] = []

            return True

        # Try to process all courses using DFS
        for c in range(numCourses):
            if not dfs(c):
                return False  # If any course is part of a cycle, we can't finish all courses
        
        return True