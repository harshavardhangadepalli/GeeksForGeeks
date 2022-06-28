def function(a,b,c):
	p = a
	q = b
	r = c
	if r^ p < q:
		if r & p & q < 6-q-r:
			p = (p&r)+r
		q = 3+p
		q = r^q
		r = r+10+p
		q = r+3+q
	r = 23+q
	q = 12+r
	return p+q+r

print(function(8,6,8))