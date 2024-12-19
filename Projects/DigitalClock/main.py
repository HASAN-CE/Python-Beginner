#Clock
import time
timestamp=(time.strftime('%H:%M:%S'))
print(timestamp)
timestamp=int(time.strftime('%H'))
print("HOURS: ",timestamp)
timestamp=int(time.strftime('%M'))
print("MINS: ",timestamp)
timestamp=int(time.strftime('%S'))
print("SEC: ",timestamp)

enter_time=int(input("ENTER CURRENT TIME IN HOURS: "))
print("CURRENT TIME IS ",enter_time,"o'clock")

if(enter_time<0):
    print("Negative time? Are you dialing in from the Upside Down?")
elif(enter_time==0):
    print("Brooo, it's 12 o'clock! Let me sleep, man!") 
elif(enter_time==1 or enter_time<6):
    print("Bro, it’s late at night—just call it a day and sleep already!")
elif(enter_time==6 or enter_time<12):
    print("GOOD MORNING SIR")
elif(enter_time==12 or enter_time<16):
    print("GOOD AFTERNOON SIR")
elif(enter_time==16 or enter_time<19):
    print("GOOD EVENING SIR")
elif(enter_time==19 or enter_time<24):
    print("GOODNIGHT SIR")
else:
    print("Bro, there are only 24 hours in a day—no extensions, deal with it!")
