from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


from HN import getData

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getData.read_json_to_db, 'interval', hours=24)
    scheduler.add_job(getData.get_data_json)
    scheduler.start()
