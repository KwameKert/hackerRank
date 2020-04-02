#Problem: 
#
#John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers 
#representing #the color of each sock, determine how many pairs of socks with matching colors there are.

#Eg = array = [1,2,1,3,2,4] output 2



def sockMerchant(n, ar):

	#create a dictionary
    holder = {}
    count = 0

  	#loop through arr
    for val in ar:
        if val in holder:
            count +=1
            del holder[val];
        else:
            holder[val] = True
    return count   


print(sockMerchant(3, [1,2,1,3,2,4]))    