from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        cnt = list(zip([-x for x in count.values()], list(count.keys())))
        heapq.heapify(cnt)
        strr = ""
        prev = ""
        while cnt:
            highest_val = heapq.heappop(cnt)
            if len(strr) != 0:
                if highest_val[1] == prev:
                    if len(cnt) == 0: return ""
                    highest_val = heapq.heapreplace(cnt, highest_val)
            
            strr = "".join([strr, highest_val[1]])
            
            highest_val = (highest_val[0] + 1, highest_val[1])
            if highest_val[0] < 0: heapq.heappush(cnt, highest_val)
            prev = highest_val[1]
        
        return strr

def main():
    ans = Solution().reorganizeString("aab") # "aba"
    ans = Solution().reorganizeString("aaab") # ""
    
    
if __name__ == "__main__":
    main()