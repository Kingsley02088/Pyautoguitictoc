fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('14'):continue
    words=licensem