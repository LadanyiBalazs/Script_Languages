#!/usr/bin/env python
# coding utf-8
 
uzenet="""
Cbcq Dgyk!
 
Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
 
Aqmimjjyi:
 
Ynyb
""" 

def main():
    msg="""
 
"""   
    for elem in uzenet:
        if elem.isupper():
            if ord(elem)>88:
                msg+=chr((ord(elem))-24)
            else:
                msg+=chr((ord(elem))+2)
        elif elem.islower():
            if ord(elem)>120:
                msg+=chr((ord(elem))-24)
            else:
                msg+=chr((ord(elem))+2) 
        else:
            msg+=elem
    print (msg)
if __name__=="__main__":
    main()