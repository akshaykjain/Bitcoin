import hashlib
import time
previousTx = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"
previousHeader = hashlib.sha256(previousTx).hexdigest()
NMax=100
NM=0

while NM<NMax:
    Target=2**(256-NM) 
    difficulty=2**NM
    maxNonce=2**32
    nextTx="I, <Chinmay Agashe>, give <Akshay Jain> 10 BTC-282, on November1,2016:"
    start_time = time.time();
    matches=0
    i=0
    while( i < maxNonce): 
         i=i+1
         stnonce=str(i);
         hash_i=hashlib.sha256(str(previousHeader) + nextTx + stnonce).hexdigest()
         if int(hash_i,16) < Target:
           end_time = time.time();
	   matches=matches+1
	   elapsed_time = end_time - start_time
	   print "For number"
           print NM
	   print "difficulty"
	   print difficulty
	   print "Matching found"
   	   print hash_i
	   print "for previousHeader =>"
	   print previousHeader
	   print "for =>NextTx"
	   print nextTx
 	   print "For nonce value"
 	   print i
	   print "Elapsed time"
	   print elapsed_time
	   print "CPU hash speed"
	   print i/elapsed_time
           print 
           break
           
         #else:
	   #print "Failed after maxNonce tries"
	   #print maxNonce
	   
    print 
    NM=NM+1 
    
