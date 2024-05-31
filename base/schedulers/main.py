from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from contextlib import asynccontextmanager
import uvicorn
from pytz import utc


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load startup logic here...
    try:
        print('Before starting application....')
        scheduler.start()
        yield
    finally:
    # Shut down logic here....
        print('After application is shut down....')
        scheduler.remove_job('my_job_id')
        print('scheduler is removed and shutdown')
        scheduler.shutdown()

# Create a FastAPI app instance
def create_app():

    app = FastAPI(lifespan=lifespan)
    return app

# Create a FastAPI app instance
app = create_app()

#dictionary for storing jobstores
jobstores = {
    'default': MemoryJobStore()
}
# Initialize an AsyncIOScheduler with the jobstore
# scheduler = AsyncIOScheduler(jobstores=jobstores, timezone='Asia/Kolkata')
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=utc)

# Job running every 3 seconds
@scheduler.scheduled_job('interval', seconds=3)
def scheduled_job_1():
    print("scheduled_job_1")

#add_job schedule method
def myjob():
    print("scheduled_job_100")

scheduler.add_job(myjob, 'interval', seconds=4, id='my_job_id')

# Job running at a specific date and time
@scheduler.scheduled_job('date', run_date='2024-04-22 22:55:50')
def scheduled_job_2():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> scheduled_job_2")
# Job running daily at 23:44:00
@scheduler.scheduled_job('cron', day_of_week='mon-sun', hour=23, minute=44, second=0)
def scheduled_job_3():
    print("scheduled_job_3")





@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


#running debug mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)