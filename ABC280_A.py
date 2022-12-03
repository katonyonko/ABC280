import io
import sys

_INPUT = """\
6
3 5
#....
.....
.##..
1 10
..........
6 5
#.#.#
....#
..##.
####.
..#..
#####
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  print(sum([S[i].count("#") for i in range(H)]))