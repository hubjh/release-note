import airflow
from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime, timedelta
import pendulum
from kubernetes.client import models as k8s

default_args = {
    'owner': 'data',
    'depends_on_past': False,
    'start_date': days_ago(1).replace(tzinfo=pendulum.timezone('Asia/Seoul'))
}

with DAG(
    dag_id='lake-release-note', 
    schedule_interval = '0 0 * * *', 
    default_args=default_args,
    max_active_runs=1,
    ) as dag:

    crawler = KubernetesPodOperator(
        name="release-note-collect",
        image="docker.items.com/release-note:latest",
        task_id="release-note-collect",
        namespace='default',
        do_xcom_push=True,
        cmds=['python3', 'collect.py'],
        get_logs=True,
        is_delete_operator_pod=False,
    )

    volume_mount = k8s.V1VolumeMount(name='spark-home',
                            mount_path='/lib/spark',
                            sub_path=None,
                            read_only=False)

    volume = k8s.V1Volume(name="spark-home", host_path=k8s.V1HostPathVolumeSource(path="/lib/spark"))
    env_vars = [k8s.V1EnvVar(name='SPARK_HOME', value='/lib/spark')]

    parser = KubernetesPodOperator(
        name="release-note-parser",
        image="docker.items.com/release-note:latest",
        task_id="release-note-parser",
        namespace='default',
        do_xcom_push=True,
        volumes=[volume],
        env_vars=env_vars,
        volume_mounts=[volume_mount],
        cmds=['/lib/spark/bin/spark-submit', 'release_note_to_yellow.py'],
        get_logs=True,
        is_delete_operator_pod=False,
    )


    sender = KubernetesPodOperator(
        name="release-note-sender",
        image="docker.items.com/release-note:latest",
        task_id="release-note-sender",
        namespace='default',
        do_xcom_push=True,
        volumes=[volume],
        env_vars=env_vars,
        volume_mounts=[volume_mount],
        cmds=['/lib/spark/bin/spark-submit', 'release_note_to_web.py'],
        get_logs=True,
        is_delete_operator_pod=False,
    )    
    
    crawler >> parser >> sender
