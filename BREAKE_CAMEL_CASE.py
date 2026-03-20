"""
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    result = ""
    
    for chr in s:
        if chr.isupper():
            result += " " + chr
        else:
            result += chr
            
    return result