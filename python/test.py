import os
import schedule
import time

def offPC():
  for i in range(11):
    print(i)
  os.system('shutdown -s')
  

schedule.every().day.at('21:00').do(offPC)

while True:
  schedule.run_pending()
  time.sleep(1)
  








