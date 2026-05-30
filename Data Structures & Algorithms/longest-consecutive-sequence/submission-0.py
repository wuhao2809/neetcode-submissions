class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort: nlogn
        # hashmap + look upward, O(n)
        consecutive_map = defaultdict(int)
        for num in nums:
            if consecutive_map[num] == 0:
                consecutive_map[num] += 1
        res = 0
        keys = list(consecutive_map.keys())
        for key in keys:
            next_key = key + 1
            while consecutive_map[next_key]:
                consecutive_map[key] += consecutive_map[next_key]
                consecutive_map[next_key] = 0
                next_key += 1
            res = max(res, consecutive_map[key])
        return res
                