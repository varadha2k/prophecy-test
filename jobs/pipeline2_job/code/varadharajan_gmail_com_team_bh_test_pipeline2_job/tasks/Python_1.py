from varadharajan_gmail_com_team_bh_test_pipeline2_job.utils import *

def Python_1():
    import json
    from datetime import timedelta
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Python_1", python_callable = None, show_return_value_in_logs = True)
