# 2125. Number of Laser Beams in a Bank
from typing import List
from collections import Counter

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0
        output = 0
        prev = 0
        cur = 0
        row1 = Counter(bank[0])
        if '1' in row1.keys():
            prev = row1['1']
        else:
            prev = 0
        for i in range(1, len(bank)):
            cur_row = Counter(bank[i])
            if '1' in cur_row.keys():
                cur = cur_row['1']
                if prev != 0:
                    mul = prev * cur
                    output += mul
                    prev = cur
                else:
                    prev = cur


        return output

if __name__ == "__main__":
    solution = Solution().numberOfBeams(bank = ["000","111","000"])
    print(solution)