from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

def SFTPSensor_1():
    from airflow.providers.sftp.sensors.sftp import SFTPSensor

    return SFTPSensor(
        task_id = "SFTPSensor_1",
        path = "path",
        sftp_conn_id = "Fabric-airflow_SFTP",
        poke_interval = 60,
        timeout = 600,
    )
