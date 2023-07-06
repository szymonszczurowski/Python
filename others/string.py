q = 'THE EYES'
print(q[:1], q[1:2], q[2:3], q[5:6], q[3:4], q[7:], q[4:5], q[6:7])

q = 'a gentelemn'
print(q[3:])
print(q[7:])
print(q[7:])
print(q[2:])
print(q[0:])
print(q[4:])
print(q[5:])
print(q[1:])
print(q[8:])

line = 'Program "Kropka nad i" nadamy o: 22:00'

time = line[line.find(':')+2:]
print(time)

tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title, time)