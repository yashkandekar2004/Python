import re 
txt ="bca management course"
x= re.search("course",txt)
print(x.string)