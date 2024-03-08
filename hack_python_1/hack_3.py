"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    result = result.capitalize()
    return result

r = fn_hack_3()
print(r)