import random 

f = [6,4,3,2,1,5,4,4,1,3,2,5,6,4,3,2,5]
f_stats=[0,0,0,0,0,0]
if i in range( len( f ) ):
  if f[i] == 1:
 f_stats[0] +=1 
  if f[i] == 2:
    f_stats[1] +=1
    if f[i] == 3: 
      f_stats[2] +=1
      if f[i] ==4: 
        f_stats[3] +=1

for i in range( len(f_stats) ):
  print(f_stats[i])    

