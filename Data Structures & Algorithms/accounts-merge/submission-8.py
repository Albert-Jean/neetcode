class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        #union sort 
        n =len(accounts)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            p = par[n]
            while p!= par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2 :
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        emailToAcc = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)  # index of acc -> list of emails
        for e, i in emailToAcc.items():
            leader = find(i)
            emailGroup[leader].append(e)

        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res
        
