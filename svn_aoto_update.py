from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os




def task():
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    os.system('svn update')
    print(local_time)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(task, 'cron', day_of_week='mon-sun', hour='0-23', minute="*", second="*/10")

    print('svnupdate ...')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'net' else 'c'))

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
