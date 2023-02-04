![Screenshot 2023-02-01 오후 4.23.11.png](https://github.com/hubjh/release-note/blob/master/Screenshot%202023-02-01%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.23.11.png)

---

### 💡 간단 소개

- 자주 사용하는 프레임워크등 기술들의 버전, 업데이트날짜, 사이트 링크 데이터를 수집하여 보여주는 웹서비스

### 💻 개발 언어

- Python

### 📆 개발 기간

- 2022/11/23 ~ 2022/12/23

### ☀️ 개발 환경

- Linux

### 👨🏻‍💻 개발 인원

- 2명

### 🔧 담당한 역할

- **데이터 수집**
    - 매일 Github API와 웹에서 Airflow로 스케쥴링하여 각 데이터소스를 JSON 파일로 수집

- **데이터 가공**
    - 수집이 끝나면 바로 JSON 데이터를 Parquet로 가공 후 테이블로 관리
    

---

## ⚙️ 사용 기술

- **Hadoop**
    - 크롤링한 데이터 소스와 Spark로 가공한 데이터 저장
- **Docker**
    - 개발단계에서 테스트용 컨테이너 생성
- **Kubernetes**
    - Spark와 Airflow가 Kubernetes에서 실행
- **Spark**
    - 수집한 데이터를 처리할 때 사용
- **Airflow**
    - 데이터 수집, 데이터 처리 스케쥴 관리

---

### 🔗 Link

[Release Note](http://15.164.106.168/?products=python,hive,spark,hadoop,airflow,prometheus,grafana,datahub,elasticsearch,delta_lake,kafka,pandas,graphql-js,rails,react,tailwind,mobx,vuex,node,django,rabbitmq,kubernetes,gatsby,tableau,flask,fastapi,seaborn,queryme,storybook,vue,express,recoil,springboot,redux,grpc,nuxt,celery,mybatis,matplotlib,angular,next,redash,nest,laravel,liquibase,emotion,spring,powerbi,numpy)
