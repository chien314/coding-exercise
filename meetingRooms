# key points:
# 0. sort starts and ends separately, which is fine 
# b/c they are constrained by the fact e_i > s_i for every given meeting
# 1. s1 < every s_i and e_i
# 2. s3 only >= s1, s2, e1, e2

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # if not intervals:
        #     return 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        
        used_rooms = 0
        end_pointer = 0

        for start_pointer in range(len(intervals)):

            if start_timings[start_pointer] < end_timings[end_pointer]:
                
                used_rooms += 1
            else:
                end_pointer += 1

        return used_rooms
