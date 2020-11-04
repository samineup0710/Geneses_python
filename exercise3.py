def to_minsec(num):
    minute = int(num/60)                #take input in second and convert into min
    rem_Sec = num -(minute *60)         #do subtract min from input to get remaining second 
    print("{}min and {}sec".format(minute, rem_Sec))  

time_sec= float(input())        #input can be in point too so do float conversion.
to_minsec(time_sec)             #function  call


    