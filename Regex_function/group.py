import re 
txt ="Technology helped us a lot in Lockdown"
x=re.search(r"\bL\w+",txt)
print (x.group())