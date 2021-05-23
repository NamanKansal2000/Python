class Solution:
    def merge(self, intervals, new_interval):
        ls = []
        for i, interval in enumerate(intervals):
            if interval.end <= new_interval.start:
                ls.append(interval)
            elif interval.start >= new_interval.end:
                ls.append(interval)
                return ls + intervals[i:]
            else:
                new_interval.start = min(interval.start, new_interval.start)
                new_interval.end = max(interval.end, new_interval.end)
        ls.append(new_interval)
        return ls

    def merge_overlaping(self, intervals):
        ls = intervals
        ls.sort(key=lambda x: x.start)
        s = []
        if ls:
            s.append(ls[0])
            for i in range(1, len(ls)):
                if ls[i].start <= s[-1].end:
                    s[-1].end = max(s[-1].end, ls[i].end)
                else:
                    s.append(ls[i])
        return ls
