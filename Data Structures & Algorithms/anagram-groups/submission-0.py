class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            item_sort = "".join(sorted(item))
            res[item_sort].append(item)
        return list(res.values())
