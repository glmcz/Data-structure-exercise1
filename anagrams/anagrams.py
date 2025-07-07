from collections import defaultdict
from typing import List


# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

class Solution:
    def groupAnagramsWithDic(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            res[sorted_str].append(s)
        return res.values()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 100:
            found: bool = False
            anagrams :List[List[str]] = []
            for sub in strs:
                sorted_sub = "".join(sorted(sub))
                if len(anagrams) == 0:
                    anagrams.append([sub])
                    continue
                for anList in anagrams:
                        if "".join(sorted(anList[0])) == sorted_sub:
                            anList.append(sub)
                            found = True
                            break
                        else:
                            found = False

                if not found:
                    anagrams.append([sub])

        return anagrams



res = Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(res)

res = Solution().groupAnagramsWithDic(["act","pots","tops","cat","stop","hat"])
print(res)