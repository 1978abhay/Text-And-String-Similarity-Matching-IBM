import pandas as pd
from array import *
def check(s, arr):
    result = True
    for i in arr:
        # for every character in char array
        # if it is present in string return true else false
        if i in s:
            result=True
        else:
            result=False
        return result

def performAlgo ( str1,  str2):
    counter = 0
    rows, cols = (len(str1)+1,len(str2) +1)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(0,len(str1)+1):
        arr[0][i]=i
       
    for i1 in range(0,len(str2)+1):
        arr[i1][0]=i1
    string = ""
    string1 = ""
    strqw = ""
    strqw1 = ""
counter =0
ans1=0
ans = 0
ans2=0
newstring = ""
string ="wat"#trying to always make first string look like second string
string1 = "woman"
temp =len(string1)
x=0
if(len(string)>len(string1)):
 number = len(string) -len(string1)
 x=1

if(len(string1)>len(string)):
 number = len(string1) -len(string)
 x=3
 for rt in range(0, number):
       string = string+" "
if(x==1):
 while((len(string)>len(string1))and ans2<temp):
        array = [string[ans2]]
        result = check(string1,array)                    
        if(result==True):
            if(string[ans2]==string1[ans2]):
                print("donothing")
            else:
                string=string[0:ans2]+string1[ans2]+string[ans2:len(string)]
                counter=counter+1
        else:
            string=string[0:ans2]+string1[ans2]+string[ans2+1:len(string)]
            counter = counter + 1
        ans2 =ans2+1
 string = string[0:temp]
 counter = counter+1
if(x==3):#len(string)<len(string1)):
    while(ans<len(string1)):#(len(string )<len(string1))and ans<len(string1)):
                    array = [string1[ans]]
                    result = check(string,array)                    
                    if(result==True):
                        if(string[ans]==string1[ans]):
                            print("donothing")
                        else:
                            print(string)
                            string=string[0:ans]+string1[ans]+string[ans:len(string)]
                            counter=counter+1
                        
                    else:
                        print("not present")
                        string=string[0:ans]+ string1[ans]+string[ans+1:len(string)]
                        counter = counter + 1
                    ans=ans+1      

while((len(string )==len(string1))and ans1<len(string1)and x!=3):  
                             
                array = [string[ans1]]
                result = check(string1,array)                    
                if(result==True):
                    print("donothing")
                else:
                    string=string[0:ans1]+ string1[ans1]+string[ans1+1:len(string)]
                    counter = counter + 1
                ans1=ans1+1           
                    
print (counter)   
        

        
        
        
             
             
str = "cl"
str1 = "cl"         
performAlgo(str, str1) 
