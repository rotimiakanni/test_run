# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:35:18 2018

@author: ROTIMI
"""

#def divisibleSumPairs(n, k, ar):
##     Complete this function
#    ans = []
#    for char in range(n):
#        for ch in range((char+1), n):
#            if (ar[char] + ar[ch])%k == 0:
#                print((char, ch))
#                po = (char, ch)
#                if po not in ans:
#                    ans.append(po)
#    return len(ans)
#            
#
#print(divisibleSumPairs(6, 3, [1,3,2,6,1,2]))

"""alternative form of inputing from stdin"""
#f = int(input())
#for d in range(0, f):
#    g = int(input())
#    print(g+5)

#f = int(input())
#for line in range(1, f+1):
#    g = input().strip().split(' ')
#    print('max fo #:' + str(line) + ': ' + max(g))


f = [["#", "d", "#", "i"], ["c", "i", "#"], ["#", "#", "K", 'k']]
u = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
def getPos(lis):
    for i_list in lis:
        chk = ''
        for x in i_list:
            chk += str(x)
        if 'k' in chk:
            return u[chk.index('k')] + str(lis.index(i_list)+1)

print(getPos(f))
#            u[i_lines.index(x)]