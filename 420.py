'''
由至少6个，至多20个字符组成。
至少包含一个小写字母，一个大写字母，和一个数字。
同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)
'''
class Solution(object):
    def strongPasswordChecker(self, s):
        lenth=len(s)
        lowers = [s[i] for i in range(len(s)) if s[i].islower()]
        uppers = [s[i] for i in range(len(s)) if s[i].isupper()]
        digits = [s[i] for i in range(len(s)) if s[i].isdigit()]
        
        typeCnt = bool(lowers) + bool(uppers) + bool(digits)

        #找出每一个字符的起始出现位置和终止出现位置
        clist = []
        li, lc = 0, (s[0] if s else None)
        for i, c in enumerate(s):
            if c != lc:
                clist.append( (lc, li, i - 1) )
                li, lc = i, c
        clist.append((lc, li, totalCnt - 1))
#统计重复字符串的个数 
#比如对于s = "aaaa333" repeats = [4, 3]
        repeats = [y - x + 1 for c, x, y in clist if y - x > 1]

        if totalCnt < 6:
            if max(repeats + [0]) == 5:
                return max(2, 3  - typeCnt)
            return max(6 - totalCnt, 3 - typeCnt)

        deleteCnt = max(totalCnt - 20, 0)

        heap = [(r % 3, r) for r in repeats]

        heapq.heapify(heap)
        while heap and totalCnt > 20:
            mod, r = heapq.heappop(heap)
            delta = min(mod + 1, totalCnt - 20)
            totalCnt -= delta
            heapq.heappush(heap, (2, r - delta))

        changeCnt = sum(r / 3 for mod, r in heap)

        return deleteCnt + max(changeCnt, 3 - typeCnt)