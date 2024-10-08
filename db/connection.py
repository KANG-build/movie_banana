# 데이터 베이스 사용 방법

# 1.Connection 맺기 (DB ------ Python 프로그램)
#  - IP      : 컴퓨터 주소
#  - Port    : 27017
#  - ID & PW : 계정정보
# 2.명령 보내기      (Python ----- DB)
# 3.결과 받기        (Python ----- DB)
# 4.Connection 끊기 (Python XXXXX DB)

# MongoDB 구조
# - MongoDB(DBMS): 데이터베이스 관리 시스템
#   ㄴ DB(NAVER): 프로젝트 단위
#       ㄴ Collection(회원) - CRUD
#       ㄴ Collection(카페) - CRUD
#       ㄴ Collection(쇼핑) - CRUD
#       ㄴ Collection(메일) - CRUD
#   ㄴ DB(KAKAO)
#   ㄴ DB(BLOG)

# MongoDB 데이터 주고받기
# - MonggoDB는 BSON Type으로 데이터를 주고 받음
# - BSON(Binary JSON) = JSON과 거의 동일
# - JSON Type으로 통일해도 문제 없음
# - Python에서 JSON은 Dict Type 사용(Python Dict = JSON)

from pymongo import MongoClient


# MongoDB Connection
def conn():  # 함수 두 줄 띄우기
    #                       mongodb_web: ip + port + id&pw
    # Python-mongodb 연결 => client
    client = MongoClient("mongodb+srv://cnu:cnu1234@moviebanana.fzjdsnm.mongodb.net/")  # IP, Port, ID&PW
    db = client["review"]  # DB 선택

    collection = db.get_collection("movie")  # Collection 선택
    return collection
