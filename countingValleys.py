def levelingValleys(n, s):
    level = 0;
    valley = 0;
    valleyCheck = False;

    
    for  val in s:
        if val == 'U':
            level = level + 1;

        if val == 'D':
            level = level - 1;
        
        if level  == 0 and  val == 'U':
            valley = valley + 1
            
    print(valley)

#    for val in s:
#        if val != "D" and val != "U":
#            raise Exception("INvalide input")
#        if val == "D":
#            if level < 0 and valleyCheck:
#                valley = valley + 1;
#                valleyCheck = False
#            level = level - 1

      
#        if val == "U":
#            if level < 0 and not valleyCheck:
#                valleyCheck = True
#            level = level + 1 

#    print(valley)        

      





levelingValleys(3,"DDUDDUUDUU")    