import datetime

# 각 모듈별 사용법은 원작자들이 매뉴얼을 만들어 두었음.
# 개별 모듈이면 그 원작자의 홈페이지를 통해서 참조
# NOT TO DO : ㅇ네이버 블로그의 남의 글 참조하기
# TO DO : 원문을 참조해야함

# 모듈명.클래스명.함수명 -> 함수 호출
current_time = datetime.datetime.now()

print('현재시간',current_time)

specific_time = datetime.datetime(2023, 6, 20, 10, 30, 00)

print('내가 만든 날짜',specific_time)