import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from varadharajan_gmail_com_team_bh_test_job_for_dev.tasks import EMRPipeline_1, S3FileSensor_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "varadharajan_gmail_com_team_BH_TEST_job_for_dev", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    S3FileSensor_0_op = S3FileSensor_0()
    EMRPipeline_1_op = EMRPipeline_1()
    S3FileSensor_0_op >> EMRPipeline_1_op
