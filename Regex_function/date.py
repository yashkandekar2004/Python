import re
text = " on 2023-09-17, the conference will begin. The event will end on 2023-09-19."

date_pattern = r"\d{4}-\d{2}-\d{2}"


dates=re.findall(date_pattern, text)
print(dates)