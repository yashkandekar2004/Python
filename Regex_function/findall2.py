
import re 
  
p = re.compile('\w') 
print(p.findall("He said * in some_lang.")) 
  
p = re.compile('\w+') 
print(p.findall("I went to him at 11 A.M., he \ said *** in some_language.")) 
  
p = re.compile('\W') 
print(p.findall("he said *** in some_language.")) 