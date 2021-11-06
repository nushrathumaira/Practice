class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        def valid(n1):
            number = str(n1)
            freq = defaultdict(int)
            #l = len(number)
            #entries = 0
            for c in number:
                freq[c] += 1

            for i in range(0,10):
                if not ( freq[str(i)] == i or freq[str(i)] == 0):
                    return False
            return True

        
        while True:
            if valid(n):
                return n
            n += 1
        return 0