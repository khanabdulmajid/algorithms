
import math
import os
import random
import re
import sys
'''
sample input
5
heater
cold
clod
reheat
docl
3
codl
heater
abcd

'''


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    anagram_dict ={}
    
    for i in range(len(query)):
        num=0
        
        for j in range(len(dictionary)):
            if len(query[i])!= len(dictionary[j]):
                print(query[i],dictionary[j])
            
            else:
                if sorted(query[i])==sorted(dictionary[j]):
                    print(query[i],dictionary[j], ' sorted')
                    num=num+1
                    anagram_dict[i]=num
            
        
    return anagram_dict


if __name__ == '__main__':
    dictionary=[]
    query=[]
    n = int(input())
    i=0
    while i<n:
        dictionary.append(input())
        i+=1
        print(i)
    m = int(input())

    i=0
    while i<m:
        query.append(input())
        i+=1

    
    anagram = stringAnagram(dictionary,query)

    for item in anagram:
        print(anagram[item])
    
