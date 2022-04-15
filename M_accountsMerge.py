               
# TC: O(N*k*logNK), where N is # of accounts and k is the # of emails in the longest sublist of the accounts array
# SC: O(N*k)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(i):
            if visited[i]:
                return 
            visited[i]=True
            
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for k in map[email]:
                    dfs(k)
                    
        visited=[False]*len(accounts)
        res=[]
        # creawte a adjacent hasmap for hmap = {email: [acc1, acc2, ...], ...}                
        map=collections.defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                map[email].append(i)
                
        for i in range(len(accounts)):
            if visited[i]:
                continue
            name, emails = accounts[i][0], set()
            dfs(i)
            res.append([name]+sorted(emails) )
            
        return res                
