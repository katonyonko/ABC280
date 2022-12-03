import io
import sys

_INPUT = """\
6
3 10
5 100
280 59
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353 
  N,P=map(int,input().split())
  dp=[0]*(N+1)
  dp[1]=1
  inv=pow(100,mod-2,mod)
  for i in range(N-1):
    dp[i+2]=(P*inv*(1+dp[i])+(100-P)*inv*(1+dp[i+1]))%mod
  print(dp[-1])