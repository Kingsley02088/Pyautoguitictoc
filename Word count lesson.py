name=input('Enter file:')
handle=open (name)
counts=dict
for line in handle:
    words=line.split()
    for word in words:
        counts[words]=counts.get(words,0) + 1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount in None or count>bigcount:
        bigword=word
        bigcount= count

print(bigword,bigcount)



