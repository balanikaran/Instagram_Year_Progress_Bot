import scriptBot
import schedule
from time import sleep

def job():
    scriptBot.main()

# job()
schedule.every().day.at("00:10").do(job)
# schedule.every(3).minutes.do(job)
while True:
    schedule.run_pending()
    sleep(1)