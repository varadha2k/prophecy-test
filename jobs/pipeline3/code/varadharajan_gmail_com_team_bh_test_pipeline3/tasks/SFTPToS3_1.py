from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def SFTPToS3_1():
    from airflow.providers.amazon.aws.transfers.sftp_to_s3 import SFTPToS3Operator

    return SFTPToS3Operator(
        task_id = "SFTPToS3_1",
        sftp_conn_id = "Fabric-airflow_SFTP",
        sftp_path = "/path",
        s3_key = "file_name",
        s3_bucket = "s3://bucket",
        s3_conn_id = "BH-Dev-AWS",
        use_temp_file = True,
    )
