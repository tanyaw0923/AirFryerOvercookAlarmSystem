import datetime
from time import sleep
tempdatetimeobj = datetime.datetime.now()

try:
    while True:
        print("#################")

        now = str(datetime.datetime.now().time()) # convert a time in string

        print("Time is:- " + str(now))

        timestring = now[:5] 
     # Slice the time for eg time is 17:02:52:23656 it will 
     slice it to 17:02 only

    print("SLICE MAGIC :- "+ timestring)

    if timestring == '17:26' :  # after slicing operation only you can compare time  

       print('Triggered')

    elif timestring == '17:30' :

       print('again triggered')

    else :
       print('-_-')        

    sleep(60)




except KeyboardInterrupt:
   print('unHandled Exception Occured')
