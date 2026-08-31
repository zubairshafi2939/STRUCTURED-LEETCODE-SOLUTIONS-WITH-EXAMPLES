class Solution(object):
    def accountsMerge(self, accounts):
        data = {}
        for x in accounts:
            if x[0] not in data:
                data[x[0]] = [x[1:]]
            else:
                data[x[0]].append(x[1:])
        return data
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
sol = Solution()
print(sol.accountsMerge(accounts))