from varadharajan_gmail_com_team_bh_test_job_for_dev.utils import *

def S3FileSensor_0():
    from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
    from datetime import timedelta

    return S3KeySensor(
        task_id = "S3FileSensor_0",
        bucket_key = [s.strip() for s in "s3://bh-d-airflow-testing/trigger/".split(",") if s.strip()],
        bucket_name = None,
        check_fn = None,
        aws_conn_id = "BH-Dev-AWS",
        wildcard_match = False,
        verify = True,
        timeout = 600,
    )
