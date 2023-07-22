
hour,minute,second=map(int,input("enter hour,minute,second:").split())
times=((hour*3600)+(minute*60)+second)

if (minute>59 or second>59):
  print("minute or seconds is wrong")
 
else:
  print("times to seconds:",times)
