"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    modified_list = []
    for char in result:
        if char.lower() in 'aeioui':
            if char.lower() == 'a':
                modified_list.append("@")
            elif char.lower() == 'e':
                modified_list.append("$")
            elif char.lower() == 'i':
                modified_list.append("1")
            elif char.lower() == 'o':
                modified_list.append("0")
            elif char.lower() == 'u':
                modified_list.append("ü")
        elif char.isalpha() == False:
            modified_list.append(char)
        else:
            modified_list.append(char.upper())
    result = modified_list        
    print(result)
    return result


fn_hack_10()