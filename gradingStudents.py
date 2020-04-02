#Grading Students


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def transformGrade(grade):
    
    remainder = grade%5
    quotient = grade//5
    nextVal = (quotient +1) * 5

   
    if abs(nextVal - grade ) <3 :
        return nextVal
    return grade


def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade >= 38 :
            grade = transformGrade(grade)
        
        result.append(grade)
      
    return result    
