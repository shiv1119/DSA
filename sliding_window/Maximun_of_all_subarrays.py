from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        q = deque()
        i = 0
        j = 0
        res = []
        while j < len(nums):

            while q and q[-1] < nums[j]:
                q.pop()
            q.append(nums[j])

            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                res.append(q[0])
                if q[0] == nums[i]:
                    q.popleft()
                i += 1
                j += 1
        return res