import io
import sys

_INPUT = """\
6
5 5 3
1 2 1
1 2 2
3 4 1
4 5 1
3 5 2
5 3
1 2
3 1
2 1 1
1 1 1
1 1
9 7 5
3 1 4
1 5 9
2 6 5
3 5 8
9 7 9
3 2 3
8 4 6
2 6
4 3
3 8
3 2
7 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def dfs(G,r):
    global parent,used,depth,root,isinf,determined
    depth[r]=0
    root[r]=r
    determined[r]=0
    st=[]
    st.append(r)
    while st:
      x=st.pop()
      if used[x]==0: continue
      used[x]=0
      for v,c in G[x]:
        if v==parent[x]: continue
        if determined[v]==0 and depth[x]+c!=depth[v]:
          isinf.add(r)
        depth[v]=depth[x]+c
        determined[v]=0
        parent[v]=x
        root[v]=r
        st.append(v)

  N,M,Q=map(int,input().split())
  G=[[] for _ in range(N)]
  for _ in range(M):
    A,B,C=map(int,input().split())
    A-=1; B-=1
    G[A].append((B,C))
    G[B].append((A,-C))

  parent=[-1]*N
  used=[-1]*N
  determined=[-1]*N
  root=[-1]*N
  depth=[-1]*N
  isinf=set()
  for i in range(N):
    if used[i]==0: continue
    dfs(G,i)

  for i in range(Q):
    X,Y=map(int,input().split())
    X-=1; Y-=1
    if root[X]!=root[Y]: print('nan')
    elif root[X] in isinf: print('inf')
    else: print(depth[Y]-depth[X])