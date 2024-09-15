from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def Slack_1():
    from airflow.providers.slack.operators.slack import SlackAPIPostOperator
    from datetime import timedelta

    return SlackAPIPostOperator(
        task_id = "Slack_1",
        text = "test",
        channel = "channel",
        slack_conn_id = "Fabric-airflow_Slack",
    )
