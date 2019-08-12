def findRelativeRanks(nums):
    pos={n:i+1 for i,n in enumerate(sorted(nums,reverse=True))}
    def f(x):
        if pos[x]==1:
            return "Gold Medal"
        elif pos[x]==2:
            return "Silver Medal"
        elif pos[x]==3:
            return "Bronze Medal"
        else:
            return str(pos[x])
    return map(f,nums)
