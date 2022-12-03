import io
import sys

_INPUT = """\
6
3 1
0 0
0 1
1 0
9 1
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
5 10000000000
314159265 358979323
846264338 -327950288
-419716939 937510582
-97494459 -230781640
628620899 862803482
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,D=map(int,input().split())
  P=[list(map(int,input().split())) for _ in range(N)]