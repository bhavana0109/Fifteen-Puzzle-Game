def prip(d):
	for i in range(len(d)):
		for j in range(len(d[i])):
			print d[i][j],
		print 	


def up(d,zc,zr):
	t=0
	if zr!=3:
		t=d[zr][zc]
		d[zr][zc]=d[zr+1][zc]
		d[zr+1][zc]=t
		prip(d)
	else:
		print "Not possible!!!"  

def left(d,zc,zr):
	t=0
	if zc!=3:
		t=d[zr][zc]
		d[zr][zc]=d[zr][zc+1]
		d[zr][zc+1]=t
		prip(d)
	else:
		print "Not possible!!!"  
  

def down(d,zc,zr):
	t=0
	if zr!=0:
		t=d[zr][zc]
		d[zr][zc]=d[zr-1][zc]
		d[zr-1][zc]=t
		prip(d)
	else:
		print "Not possible!!!"  

def right(d,zc,zr):
	t=0
	if zc!=0:
		t=d[zr][zc]
		d[zr][zc]=d[zr][zc-1]
		d[zr][zc-1]=t
		prip(d)
	else:
		print "Not possible!!!"  


def check(d):
	if d==[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]:
		print "You WON!!!"
		return 1
	return 0
	
	
global d
d=[[8,1,15,10],[5,4,14,2],[6,9,12,3],[7,13,11,0]]
prip(d)

c=0
while c!=1:
  f=0
  op=raw_input()	
  for i in range(len(d)):
		for j in range(len(d[i])):
			if d[i][j]==0:
				zr=i
				zc=j
				f=1
				break
		if f==1:
			break
	
  
  if op=="w":
		up(d,zc,zr)
		c=check(d)
	
  elif op=="a":
		left(d,zc,zr)
		c=check(d)
	
  elif op=="s":
		down(d,zc,zr)
		c=check(d)
	
  else:
		right(d,zc,zr)
		c=check(d)
		
	
	