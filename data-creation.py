"""
Create:
    - Csv file for DL with folder structure /year/month/day and columns ID,
    Status (OPEN, IN_PROGRESS, CLOSED, REMOVED). Must be visible in DW using 
    view 'PipelineReport' with the additional columns year, month, day.
    - MimosaStatus table in DW contains cols ID, Status.
"""
import uuid
import random
import os
import datetime


STATUSES = ["OPEN", "IN_PROGRESS", "CLOSED", "REMOVED"]

# Keep all uuids that are create in global valiable so they can be used in each
# table
uuids = []

def create_pipeline_report_csv(n_rows: int, filepath_prefix: str) -> None:
    for _ in range(n_rows):
        _id = uuid.uuid4()
        uuids.append(_id)
        with open(os.path.join(filepath_prefix, "piplinereport.csv"), "a") as csv_file:
            csv_file.write(f"{_id},{random.choice(STATUSES)}\n")
    

def create_csv_files() -> None:
    start = datetime.date(2018, 1, 1)
    end = datetime.date(2022, 6, 15)
    date = start
    while date <= end:
        prefix = f"pipeline-report/{date.year}/{date.month}/{date.day}"
        if not os.path.exists(prefix):
            os.makedirs(prefix)
        create_pipeline_report_csv(random.randint(5, 15), prefix)

        date += datetime.timedelta(days=1)


def create_DW_info_as_csv():
    os.mkdir("mimosa-status")
    with open("mimosa-status/MimosaStatus.csv", "a") as csv_file:
        csv_file.write(f"ID,Status\n")
    
    for _id in uuids:
        with open("mimosa-status/MimosaStatus.csv", "a") as csv_file:
            csv_file.write(f"{_id},{random.choice(STATUSES)}\n")


create_csv_files()
create_DW_info_as_csv()
    
