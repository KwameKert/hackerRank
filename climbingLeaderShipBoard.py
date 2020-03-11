# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    if len(scores) < 1 or len(scores) > 2*(10**5):
        raise Exception("invalid input for scores")

    if len(alice) < 1 or len(alice) > 2*(10**5):
        raise Exception("invalid input for alice") 


    
    #print(sorted(scores, reverse=True));    
    if scores != sorted(scores, reverse=True):
        raise Exception("Invalid scores")

      
    if alice != sorted(alice):
        raise Exception("invalid alice")

    response = list();


    setScores = set(scores);
    listScore = sorted(list(setScores),reverse=True);
    sortLst = sorted(listScore)
    

    cache = {}
    optList = []
    for val in alice:     
       if val < 1 or val >10**9:
        raise Exception("Invalid input") 
       
       if val in cache:
            response.append(cache[val])
            continue
        
       if val > listScore[0]: 
            cache[val] = 1;
            response.append(1)
            continue

       if val < listScore[-1]:
            cache[val] = len(listScore)+1;
            response.append(len(listScore)+1)
            continue

       reverseList = sorted(listScore, reverse=True)
       
       for idx,x in enumerate(reverseList):

            #print(idx,x,val,optList)
            if x < 1 or x >10**9:
                raise Exception("Invalid input") 

            if val == x:
                cache[val] = idx+1;
                response.append(idx+1);
                reverseList = reverseList[idx+1:]
                print(reverseList)
                break

            if val < x and val > reverseList[idx+1]:
                cache[val] = idx+2
                response.append(idx+2)
                reverseList = reverseList[idx+1:]
                print(reverseList)
                break
        
    return response;