import datetime
from sg import SignalsGenerator
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=1)
def timed_job():
    print("{0} signals generator running...".format(datetime.datetime.utcnow()))
    SignalsGenerator.run()


scheduler.start()