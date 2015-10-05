f = open('dictionary.dic', 'r')
f2 = open('words', 'w')
l = set()
for i in f:
    if (len(i.split('(')) >1):
        l.add(i.split('(')[0])
    else:
        l.add(i.split(' ')[0])


for item in l:
  f2.write("%s\n" % item)
