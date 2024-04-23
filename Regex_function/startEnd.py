import re 
txt ="Technology helped us a lot in Lockdown"
x=re.search(r"\bL\w+",txt)
print("Starting index:",x.start())
print("Ending index:",x.end())