import io
import sys

_INPUT = """\
6
atcoder
atcorder
million
milllion
vvwvw
vvvwvw
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  T=input()
  ans=1
  for i in range(len(S)):
    if S[i]!=T[i]:
      break
    else: ans+=1
  print(ans)