s = "django"
print(s[0],s[5],s[:4],s[1:4],s[4:],s[::-1],sep='\n')
print()
l = [3, 7, [1, 4, 'hello']]
l[2][2]="goodbye"
print(l)
print()
m = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(m['k1'][0]['nest_key'][1][0])
print()
ll = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(set(ll))
