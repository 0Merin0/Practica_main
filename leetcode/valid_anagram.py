from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = Counter(t)

        for c in s:
            if c not in d:
                return False
            d[c] -= 1

        return all(True if v == 0 else False for v in d.values())


if __name__ == "__main__":
    print(Solution().isAnagram("aacc", "ccac"))
