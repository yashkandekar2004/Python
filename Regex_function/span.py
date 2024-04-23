import re 
txt ="python i good to learn "
x =re.search (r"\bt\w+", txt)
print("t appears at position :", x.span())