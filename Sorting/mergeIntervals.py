class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n_intervals = len(intervals)
        #print(n_intervals)
        out = []
        for i in sorted(intervals, key=lambda i:i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1],i[1])
            else:
                out.append(i)
        return out