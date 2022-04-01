from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="063"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc075_b".format(times, problem)) as res:
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
  N,A,B=map(int,input().split())
  H=[int(input()) for _ in range(N)]
  l,r=0,10**10
  while r-l>1:
    mid=(l+r)//2
    tmp=sum([max(0,(H[i]-mid*B-1)//(A-B)+1) for i in range(N)])
    if tmp>mid: l=mid
    else: r=mid
  print(r)
  """ここから上にコードを記述"""

  print(test_case[__+1])