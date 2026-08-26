class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-","").upper()
        ans = []
        for i in range(len(s), 0, -k):
            j = max(0,i-k)
            ans.append(s[j:i])
        ans.reverse()
        return "-".join(ans)

        