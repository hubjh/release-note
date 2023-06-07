# 릴리즈 노트

# ☑︎ 프로젝트 결과

---

![Screenshot 2023-02-01 오후 4.23.11.png](https://github.com/hubjh/release-note/blob/master/Screenshot%202023-02-01%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.23.11.png)

### 🔗 Link

[http://15.164.106.168/?products=python,hive,spark,hadoop,airflow,prometheus,grafana,datahub,elasticsearch,delta_lake,kafka,pandas,graphql-js,rails,react,tailwind,mobx,vuex,node,django,rabbitmq,kubernetes,gatsby,tableau,flask,fastapi,seaborn,queryme,storybook,vue,express,recoil,springboot,redux,grpc,nuxt,celery,mybatis,matplotlib,angular,next,redash,nest,laravel,liquibase,emotion,spring,powerbi,numpy](http://15.164.106.168/?products=python,hive,spark,hadoop,airflow,prometheus,grafana,datahub,elasticsearch,delta_lake,kafka,pandas,graphql-js,rails,react,tailwind,mobx,vuex,node,django,rabbitmq,kubernetes,gatsby,tableau,flask,fastapi,seaborn,queryme,storybook,vue,express,recoil,springboot,redux,grpc,nuxt,celery,mybatis,matplotlib,angular,next,redash,nest,laravel,liquibase,emotion,spring,powerbi,numpy)

## **결과의 의미**

|  | 개인 | 팀 |
| --- | --- | --- |
| 얻은 것 |  | 필요한 프레임워크의 버전 정보를 볼 수 있는 웹페이지가 생겼다.

데이터 플랫폼 서버의 테스트를 위한 데이터 파이프라인을 추가 |

# ✎ 프로젝트 배경

---

| 프로젝트 인원 | 2명 |
| --- | --- |
| 프로젝트의 목표 | 프레임워크들의 릴리즈 노트 정보를 보여주는 웹페이지에서 사용할 파이프라인 구축 |
| 팀의 목표 | 데이터플랫폼 서버의 인프라 성능, 안정성 테스트

1. k8s에 pod로 올려놓은 Spark, Airflow 등이 안정적으로 작동하는지 테스트
2. k8s 노드들의 리소스(CPU, Memory) 이상 테스트
3. 이상 발견 시 문제점을 해결한다. |
| 팀 내 나의 역할  | 1. Github API를 활용한 파이프라인 Python 스크립트 만들기
2. Airflow를 통해 Python 스크립트들의 스케쥴 작성 |
| 팀의 문제 혹은 기회 상황 | 프로젝트
1. 프론트를 할 줄 아는 사람이 없으므로 서비스 웹페이지는 외주를 맡겨서 만든다.
2. 서비스용으로 사용 가능한 Amazon lightsail 서버가 있다.
3. lightsail 서버에서 동작하는 백엔드 기능은 팀장이 만든다. |
| 개발 기간 | 2022.11 ~ 2022.12 |
| 개발 언어  | Python |
| 개발 환경 | 온프레미스 환경 Ubuntu:20.04 |
| 사용 기술
 | Main : 주로 사용한 기술

• Hadoop
    ◦ 수집한 채팅로그, streams 데이터 소스와 Spark로 가공한 데이터 저장
• Docker
    ◦ 개발 단계에서 테스트용 컨테이너 생성
• Spark
    ◦ 수집한 데이터를 필터링 할 때 사용
• Airflow
    ◦ Spark 실행 스케쥴 관리 |

# 🧩 프로젝트 과정

---

# 조사내용

# Github API

---

# Ex)

| vue.js의 github 데이터를 보여주는 API |
| --- |
| https://api.github.com/repos/vuejs/vue/releases |

### https://api.github.com/repos/{`owner`}/{`repo`}/releases

| 경로 매개 변수 | Type | 필수 매개 변수 | 설명 |
| --- | --- | --- | --- |
| owner | string | 필수 | 저장소의 계정 소유자입니다. 이름은 대소문자를 구분하지 않습니다. |
| repo | string | 필수 | 리포지토리의 이름입니다. 이름은 대소문자를 구분하지 않습니다. |

## 수집하는 데이터

| tag_name | GitHub에서 릴리스에 할당된 태그(Tag)의 이름 |
| --- | --- |
| html_url | GitHub에서 해당 릴리스에 대한 웹 페이지 URL |
| published_at | GitHub에서 릴리스가 게시된 날짜와 시간을 나타내는 타임스탬프 |

# 프로그램 동작

---

1. 매일 0시 0분에 Python 스크립트 파일을 Airflow로 스케쥴링하여 프레임워크 버전, 웹 페이지 URL, 게시된 날짜를 수집
2. 수집한 데이터를 Parquet로 가공 후 yellow 테이블로 관리
3. yellow 테이블에서 SQL로 데이터 추출 후 lightsail 서버에 API로 전송
4. lightsail 서버에서 Docker 컨테이너로 서비스 웹페이지에 데이터 갱신

# Airflow DAG

---

| schedule_interval | 0 0 * * *  |
| --- | --- |
| DAG | Crawler >> Parser >> Sender |

## Crawler

| Operator | KubernetesPodOperator |
| --- | --- |
| cmds | [‘python3’, ‘foo.py’] |
| 기능 | 1. Github API로 프레임워크들의 버전 정보들을 수집
2. Github에서 구할 수 없는 프레임워크들의 버전 정보를 수집

HDFS에 JSON으로 포맷 |

## Parser

| Operator | KubernetesPodOperator |
| --- | --- |
| cmds | [‘/bin/spark-submit’, ‘bar.py’] |
| 기능 | red 테이블에서 필요한 데이터만 뽑아서 Spark로 중복 제거, 스키마 부여
HDFS에 parquet으로 포맷 |

## Sender

| Operator | KubernetesPodOperator |
| --- | --- |
| cmds | [‘/bin/spark-submit’, ‘baz.py’] |
| 기능 | yellow 테이블에서 spark sql로 필요한 데이터 추출
추출 데이터를 Amazon lightsail 서버에 API로 전송 |

## Amazon lightsail

---

Amazon lightsail에서 Docker 컨테이너로 Fast API 서버가 동작
Sender로 받은 데이터를 로컬에 저장하고 웹페이지에 갱신하는 기능을 한다.
