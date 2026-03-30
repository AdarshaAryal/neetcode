"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start) # T: O(nlogn), S: O(1)

        def does_overlap(a, b): # T: O(1)
            return a.end > b.start
        
        for index in range(len(intervals) - 1): # T: O(n)
            first = intervals[index]
            second = intervals[index + 1]
            if does_overlap(first, second):
                return False
        
        return True