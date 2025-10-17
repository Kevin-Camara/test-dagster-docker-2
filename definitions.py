from dagster import Definitions, asset, job, schedule

@asset
def my_asset():
    return "Hello from new project"

@job
def my_job():
    my_asset()

@schedule(job=my_job, cron_schedule="0 0 * * *")
def my_schedule():
    return {}

defs = Definitions(
    assets=[my_asset],
    jobs=[my_job],
    schedules=[my_schedule]
)
