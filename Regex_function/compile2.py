import re 
p = re.compile('\d') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
  
p = re.compile('\d+') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 