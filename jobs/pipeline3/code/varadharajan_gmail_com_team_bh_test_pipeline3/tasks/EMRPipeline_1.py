from varadharajan_gmail_com_team_bh_test_pipeline3.utils import *

@task_wrapper(task_id = "EMRPipeline_1")
def EMRPipeline_1(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.amazon.aws.operators.emr import (EmrAddStepsOperator, ) # noqa

    return EmrAddStepsOperator(
        task_id = "EMRPipeline_1",
        job_flow_id = "j-11FIPPFJGAJE9",
        aws_conn_id = "aws_default",
        steps = [{
           "Name": "pipelines_pipeline1", 
           "ActionOnFailure": "CONTINUE", 
           "HadoopJarStep": {
             "Jar": "command-runner.jar", 
             "Args": ["spark-submit",  "--deploy-mode",  "cluster",  "--executor-memory",  "1g",  "--executor-cores",  "1",                        "--num-executors",  "1",  "--driver-memory",  "1g",  "--driver-cores",  "1",  "--conf",                        "spark.prophecy.metadata.job.uri=__PROJECT_ID_PLACEHOLDER__/jobs/pipeline3",                        "--conf",  "spark.prophecy.metadata.is.interactive.run=false",  "--conf",                        "spark.prophecy.metadata.fabric.id=16995",  "--conf",                        "spark.prophecy.tasks=H4sIAAAAAAAAAKuuBQBDv6ajAgAAAA==",  "--conf",                        "spark.prophecy.metadata.url=__PROPHECY_URL_PLACEHOLDER__",  "--conf",                        "spark.prophecy.metadata.user.id=6313",  "--conf",                        "spark.prophecy.project.id=__PROJECT_ID_PLACEHOLDER__",  "--conf",                        "spark.prophecy.execution.metrics.disabled=true",  "--conf",                        "spark.prophecy.metadata.job.branch=__PROJECT_RELEASE_VERSION_PLACEHOLDER__",                        "--conf",                        "spark.prophecy.execution.service.url=wss://execution.dp.app.prophecy.io/eventws",                        "--jars",                        "s3://prophecy-public-bucket/prophecy-libs/prophecy-libs-assembly-3.4.0-8.0.31.jar",                        "--py-files",                        "s3://prophecy-public-bucket/python-prophecy-libs/prophecy_libs-1.9.9-py3-none-any.whl,s3://prophecy-public-bucket/python-prophecy-libs/pyhocon-0.3.60-py3-none-any.whl,s3://prophecy-public-bucket/python-prophecy-libs/pyparsing-3.1.0-py3-none-any.whl,s3://prophecytesting/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline1-1.0-py3-none-any.whl",                        "s3://prophecytesting/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/pipeline1/launcher.py",                        "-i",  "default",  "-O",  "{}"]
           }
         }],
    )
