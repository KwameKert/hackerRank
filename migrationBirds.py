#You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.
#For example, assume your bird sightings are of types . There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type


#sample
#  Input 1 4 4 4 5 3
# Output 4

#def migratoryBirds(arr):
 #   holder = {}
    #sort array in ascending order
  #  arr.sort()

    #loop through array
   # for item in arr:
    #place the items in hash table with their counts
    #    if item in holder:
     #       holder[item] =  holder[item]+1;
      #  else:
       #     holder[item] =1

    #get highest count
   # return max(holder, key=holder.get)


def migratoryBirds(arr):

    #define an array of 6 elements
    count = [0]*6

    #loop through an array and increase the value of an index
    for item in arr:
        count[item] = count[item]+1

    #return the max number in the array and return its index
    return count.index(max(count))





print(migratoryBirds([1, 4, 4, 4, 5, 3]))
print(migratoryBirds([2, 2, 1, 1]))
print([0]*5)
