# 🛍 Walmart 고객 관리 페이지 프로젝트

![walmart](https://github.com/user-attachments/assets/472e79e8-fb84-467e-93e0-3e8b64f56aed)

## Index

- [Introduction](#simple-description)
- [Overview](#overvie)
- [Contributing](#contributing)



## 1. 프로젝트 개요
이 프로젝트는 Django 기반으로 월마트 고객 관리 및 판매 데이터를 분석하는 웹 페이지입니다. 고객의 정보를 관리하고, 구매 내역을 조회 및 분석하며, 판매 통계를 시각화하는 기능을 제공합니다.

<br>

## 2. 주요 기능
- 관리자 로그인 권한: 관리자는 로그인 후 고객 관리 및 통계 대시보드를 이용할 수 있습니다.
- 고객 목록 조회: 시스템에 등록된 모든 고객 목록을 조회할 수 있습니다.
- 고객 추가, 수정, 삭제: 고객의 정보를 추가, 수정, 삭제할 수 있습니다.
- 고객 판매 상세 페이지: 각 고객의 구매 내역을 조회할 수 있습니다.
- 판매 통계 및 시각화:
  - 기간별, 월별, 연도별 판매액 분석
  - 제품 카테고리별, 나이별, 성별별 판매액 분석
  - 분석 결과를 차트로 시각화하여 데이터 직관적으로 제공

<br>

## 3. 화면 구상도

![image](https://github.com/user-attachments/assets/4a31752c-a1e8-4391-9ad6-f643e09177b5)

화면 구상도 링크 : [https://whimsical.com/crm-project-JVrvnk65BKwgijV1WEttbN]

<br>

## 4. 기술 스택
- 프레임워크: Django
- 데이터베이스: SQLite
- 프론트엔드: HTML, CSS
- 차트 시각화: Chart.js
- 기타: Python

<br>

## 5. 문제 및 해결 과정
- DB 충돌 및 동기화 문제 <br>
동시에 작업하면서 데이터베이스 마이그레이션 파일(migrations)에 충돌이 발생하거나, 로컬 DB와 원격 DB 간의 불일치로 인해 동기화 문제가 발생했지만 마이그레이션 충돌을 방지하기 위해 작업 전후로 python manage.py makemigrations 명령어를 실행하고, 마이그레이션 파일이 충돌하지 않도록 협의했습니다. 최종적으로 python manage.py migrate 명령어를 실행해 DB가 최신 상태로 동기화되도록 했습니다.
 
- git 충돌 문제 (Pull/Push) <br>
  git push 후 다른 팀원이 git pull을 할 때, 코드 충돌이 발생하거나 최신 버전의 코드가 반영되지 않는 문제가 발생했지만 팀원과 작업 전후로 작업한 파일을 명확히 공유하고, 충돌이 예상되는 부분에 대해 미리 알리며 작업을 진행했습니다.
  미리 작업 단위를 분리 하며 충돌을 최소화하기 위해 각 팀원이 작업할 영역을 분리하고, 각 기능을 독립적으로 구현 후 병합하는 방식으로 진행하였습니다
  만약 충돌이 발생하면, 직접 git merge를 통해 충돌을 해결하고, 커밋 메시지에 충돌 해결 과정을 기록하였습니다

<br>

## 6. 프로젝트 링크
[https://github.com/EunSeo35/django-crm-project]


## Contributing
<p>
<a href="https://github.com/EunSeo35">
    <img src="https://avatars.githubusercontent.com/EunSeo35" width="90">
</a>
<a href="https://github.com/selina7704">
    <img src="https://avatars.githubusercontent.com/selina7704" width="90">

