"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    for i in range(6):
        result.append(i)
    result = sorted(result,reverse=True)
    return result  

r = fn_hack_7()
print(r)