class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find(parents, node):
            if node==parents[node]:
                return node
            parents[node]= find(parents, parents[node])
            return parents[node]

        def union(parents, size, a, b):
            a=find(parents, a)
            b=find(parents, b)
            if a!=b:
                if size[a] > size[b]:
                    size[a] += size[b]
                    parents[b] = a
                else:
                    size[b] += size[a]
                    parents[a] = b
                return 1
            return 0

        parents = list(range(n))
        size = [1] * n
        
        logs.sort(key=lambda log:log[0])
        tot=n-1
        for l in logs:
            tot-=union(parents,size,l[1],l[2])
            if tot==0:
                return l[0]
        return -1