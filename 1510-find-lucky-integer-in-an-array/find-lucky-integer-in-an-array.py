class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
        max_luck =  -1
        for num,count in hashmap.items():
            if num == count:
                max_luck =  max(max_luck, num)
        return max_luck

        