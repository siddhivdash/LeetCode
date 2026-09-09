class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        Holdmydick = 1000
        while n >= Holdmydick:
            count += n- Holdmydick + 1
            Holdmydick *= 1000
        return count 

        