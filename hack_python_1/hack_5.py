"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result.replace("fooziman","f00z1m@n")
    return result  

r = fn_hack_5()
print(r)