import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
coefficient of determination: 0.715875613747954
  
print('intercept:', model.intercept_)
print('slope:', model.coef_)

new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print('intercept:', new_model.intercept_)
print('slope:', new_model.coef_)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

y_pred = model.intercept_ + model.coef_ * x
print('predicted response:', y_pred, sep='\n')

x_new = np.arange(5).reshape((-1, 1))
print(x_new)

y_new = model.predict(x_new)
print(y_new)

import datetime
import winsound  # exclusively for windows only,
# if you are on any other system you can use 'playsound' or 'simpleaudio' module.

alarm_hour = int(input("Set hour: "))
alarm_minutes = int(input("Set minutes: "))
am_pm = input("am or pm? ")

print(f"Waiting for time: {alarm_hour}:{alarm_minutes} {am_pm}")

# time conversion
# because datetime module returns time in military form i.e. 24 hrs format
if am_pm == 'pm':  # to convert pm to military time
    alarm_hour += 12

elif alarm_hour == 12 and am_pm == 'am':  # to convert 12am to military time
    alarm_hour -= 12

else:
    pass

while True:  # infinite loop starts to make the program running until time matches alarm time

    # ringing alarm + execution condition for alarm
    if alarm_hour == datetime.datetime.now().hour and alarm_minutes == datetime.datetime.now().minute:

        print("\nIt's the time!")
        winsound.Beep(1000, 1000)
        break
