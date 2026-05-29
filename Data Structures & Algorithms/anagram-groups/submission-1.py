class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort + hashmap
        # bucket sort
        groups_dict = defaultdict(list)
        for each in strs:
            groups_dict["".join(sorted(each))].append(each)
        return list(groups_dict.values())
