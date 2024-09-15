from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def Email_1():
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_1",
        to = "test@test.com",
        subject = "test",
        html_content = "test content",
        cc = None,
        bcc = None,
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "Fabric-airflow_Email",
    )
