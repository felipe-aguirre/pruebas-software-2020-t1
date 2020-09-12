def compareString(a,b):
	valid = [0,0]
	if type(a) is str:
		valid[0] = 1
	if type(b) is str:
		valid[1] = 1
	if valid == [1,1]:
	    if len(a) > len(b):
	    	return a
	    else:
	    	return b
	else:
		return valid		
