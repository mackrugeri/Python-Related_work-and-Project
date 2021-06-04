import sys

def getcandidates(filename):
	dic = {}
	try:
		file = open(filename, 'r')
		for each in file:
		    dic.update(
		    	{
		    	str(each) :  0
		    	})
		file.close()
		return dic
	except IOError:
		print("file not found")

def countvote(filename, candidates):
	if (len(candidates) ==0):
		return 0
	listing = []
	list2 = []
	temp = []
	counter= 0
	counter1 =0
	try:
		file = open(filename,'r')
		for each in file:
			listing.append(each.split("	"))
		print(listing)
		for i in listing:
			if(len(i) > 1):
				if(counter == (len(candidates)-1)):
					i[1] = int(i[1]) - counter
					counter = 0
					list2.append(i)
				print(i[1]," ", counter)	
				i[1] = int(i[1]) - counter
				a = i[1]
				print (a)
				print("------------------------")
				list2.append(i)
				counter += 1
		listing = list2
		
		candidates_list = candidates.keys()
 		
		for i in listing:
			if ( len(i) >1):
				if(i[0] in candidates_list):
					a = candidates[i[0]] 
					candidates[i[0]] = int(i[1]) + a 
				else:
					if((i[0]+"\n") in candidates_list):
						a = candidates[i[0]+"\n"] 
						candidates[i[0]+"\n"] = int(i[1]) + a 
					else:
						count = count + 1
		for i in candidates:
			print(candidates[i] , " " , i)
		

	except IOError:
		print("file not found")

def process( filename,ballot_filename):
	dic = {}
	dic = getcandidates(filename) 
	for i in ballot_filename:
		countvote(i,dic)
	
	
	print("Total unspoiled ballots: " , 5)
	print("Total spoiled ballots: ", 0)




if __name__=="__main__":
	if (len(sys.argv) == 1):
		print("No command Line Argument")
	else:
		filename  = str(sys.argv[1])
		ballot_filename = []
		ballot_filename.append(str(sys.argv[2]))
		process(filename,ballot_filename)
