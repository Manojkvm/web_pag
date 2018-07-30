"""def array_check(seq):
    for i in range(len(seq)-2):
        if(seq[i] == 1 and seq[i+1] == 2 and seq[i+2] == 3 ):
            return True
    return False


print(array_check([1,1,1,2,3,2]))
print(array_check([1,1,1,2,2,1]))
array_check([1,2,1,2,3,1,1])
"""
"""def str_bits(ss):
    x = ""
    for i in range(0,(len(ss)),2):
        x+=ss[i]
    print(x)

str_bits('hello')
str_bits('hi')
str_bits('heeololwo')
"""
"""def end_other(a,b):
    a = a.lower()
    b = b.lower()
    return (a.endswith(b) or b.endswith(a))
    return a[-(len(b)):]== b or b[-(len(a)):]== a

print(end_other('abc','gwabC'))
print(end_other('adAbC','Hrhs'))
"""
"""def double_str(a):
    x = ""
    for i in a:
        x = x + i*2
    print(x)

double_str('The')
double_str('AAbb')
"""
"""def even(seq):
    x = 0
    for i in seq:
        if i%2==0:
            x=x+1
    print(x)

even([1,2,38,4,7,8])
even([0,2,4])
even([1,3,5])
"""
