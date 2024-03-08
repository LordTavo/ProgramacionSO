"""
text: "FOOZIMAN" output => "fooziman"
"""

def fn_hack_2():
    result = "FOOZIMAN"
    result = result.lower()
    return result

r = fn_hack_2()
print(r)