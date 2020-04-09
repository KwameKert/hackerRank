#climbing the leaderboard
def checkPosition(score,hashScore):
     rank = 0;
     for item in hashScore:
         if score >= item:
             return hashScore[item]
         else:
             rank = hashScore[item]
     return rank+1


def climbingLeaderboard(scores,alice):
     #load scores into hashtable
     scoresHash = {}
     rank = 1;
     alicePositions = [];
     for item in scores:
         if item not in scoresHash:
             scoresHash[item] =  rank;
             rank += 1
     #looping through alice values
     for val in alice:
         aliceRank = checkPosition(val,scoresHash)
         #print(aliceRank)
         alicePositions.append(aliceRank)
     return alicePositions;


result = climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102])
print(result)

