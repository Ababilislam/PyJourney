import sched
import time
from datetime import datetime

# scheduler = sched.scheduler(time.time, time.sleep)
#
# def schedule_event(name,start):
#     now = time.time()
#     elapsed = int(now-start)
#     print("elepsed = ",elapsed, 'name= ',name)
#
#
# stat = time.time()
# print("START:",time.ctime(stat))
# scheduler.enter(2,1,schedule_event,("event-1",stat))
# scheduler.enter(5,1,schedule_event,("event-2",stat))
#
# scheduler.run()


#     second scheduler to understand better /////////

def adition(a,b):
    print("performing addition:",datetime.now())
    print("time: ",time.monotonic())
    print("result:",a+b)

s = sched.scheduler()

print("start Time: ",datetime.now())

event1= s.enter(10,1,adition,argument=(5,6))
print("event created :",event1)
s.run()
print("end time",datetime.now())