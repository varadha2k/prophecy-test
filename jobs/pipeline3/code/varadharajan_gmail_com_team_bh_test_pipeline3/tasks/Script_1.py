from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def Script_1():
    from airflow.operators.bash import BashOperator

    return BashOperator(
        task_id = "Script_1",
        bash_command = "#!bash",
    )
