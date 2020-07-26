from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler
from auto import send_msg

sched = BlockingScheduler()




sched.add_job(job_function, 'interval',hours=2)

sched.start()