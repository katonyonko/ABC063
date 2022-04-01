from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="063"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc075_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  S=[int(input()) for _ in range(N)]
  dp=[[0]*10001 for _ in range(N+1)]
  dp[0][0]=1
  for i in range(N):
    dp[i+1]=dp[i].copy()
    for j in range(10001):
      if j+S[i]<10001 and dp[i][j]==1: dp[i+1][j+S[i]]=1
  if len([i for i in range(10001) if dp[-1][i]==1 and i%10!=0])==0: print(0)
  else: print(max([i for i in range(10001) if dp[-1][i]==1 and i%10!=0]))
  """ここから上にコードを記述"""

  print(test_case[__+1])