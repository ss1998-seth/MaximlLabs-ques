
NO = 256
def maximum_char(str, n): 

	count = [0] * NO 

	for i in range(n): 
		count[ord(str[i])] += 1
	
	max_distinct = 0
	for i in range(NO): 
		if (count[i] != 0): 
			max_distinct += 1	
	
	return max_distinct 

def smallestSubstring(str): 

	n = len(str)	
	max_distinct = maximum_char(str, n) 
	minl = n	 
	for i in range(n): 
		for j in range(n): 
			subs = str[i:j] 
			subs_length = len(subs) 
			sub_distinct_char = maximum_char(subs, 
												subs_length) 
			
			if (subs_length < minl and
				max_distinct == sub_distinct_char): 
				minl = subs_length 

	return minl 

# Driver Code 
if __name__ == "__main__": 
	
	# Input String 
	str = input("enter a string")
	
	l = smallestSubstring(str); 
	print( "The length of the smallest required substring : ",  l) 

