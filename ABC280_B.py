import io
import sys

_INPUT = """\
6
3
3 4 8
10
314159265 358979323 846264338 -327950288 419716939 -937510582 97494459 230781640 628620899 -862803482
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=list(map(int,input().split()))
  print(*[S[0]]+[S[i+1]-S[i] for i in range(N-1)])