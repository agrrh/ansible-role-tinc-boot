#!/usr/bin/env python3
print("|","Variable","|","Default value","|","Description","|")
print("|","--------","|","-------------","|","-----------","|")
comment = []
with open('defaults/main.yml', 'rt') as f:
    for line in f:
        line = line.strip()
        if line == "":
            comment = []
            continue
        if line.startswith('#'):
            comment.append(line.strip('#'))
        else:
            key, value = line.split(':', 1)
            print("|",key,"|",value,"|"," ".join(comment),"|")
            comment = []