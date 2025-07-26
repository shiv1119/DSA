#User function Template for python3
from collections import Counter
class Solution:
	def search(self,pat, txt):
	    k = len(pat)
		m = Counter(pat)
		count_m = len(m)
	    anagram_count = 0
	    i = 0
	    j = 0
	    
	    while j < len(txt):
	        if txt[j] in m:
	        	m[txt[j]] -= 1
	            if m[txt[j]] == 0:
	            	count_m -= 1
	        
	        if j-i+1 < k:
	        	j += 1
	        elif j-i+1 == k:
	            if count_m == 0:
	            	anagram_count += 1
	            
	            if txt[i] in m:
	                m[txt[i]] += 1
	                if m[txt[i]] == 1:
	                    count_m += 1
	        	i += 1
	        	j += 1
	            
		return anagram_count
	   
	    