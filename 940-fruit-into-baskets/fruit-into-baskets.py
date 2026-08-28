class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_fru = 0
        left = 0 
        for i in range(len(fruits)):
            basket[fruits[i]] = basket.get(fruits[i], 0) +1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                left += 1
            max_fru = max(max_fru, i - left + 1)
        return max_fru
