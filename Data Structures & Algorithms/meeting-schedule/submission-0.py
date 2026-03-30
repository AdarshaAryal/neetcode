"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)

        def does_overlap(a, b):
            return a.start < b.end and b.start < a. end
        
        for index in range(len(intervals) - 1):
            first = intervals[index]
            second = intervals[index + 1]
            if does_overlap(first, second):
                return False
        
        return True