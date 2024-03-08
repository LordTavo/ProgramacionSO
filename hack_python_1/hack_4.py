"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    ultima_letra = result[-1:].upper()
    result = result[:-1] + ultima_letra
    return result

r = fn_hack_4()
print(r)