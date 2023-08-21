import logging
import argparse

# 로거 정의
logger = logging.getLogger('my-logger')

# 로그레벨 설정
logging.basicConfig(level = logging.DEBUG) # level에 내가 출력하고 싶은 로그레벨 작성 ex) logging.WARNING, logging.ERROR 등

# 로그 포맷팅
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # 글자를 포멧탕하는 방법 '%(variable)s'
handler1 = logging.StreamHandler() # 화면에 로그를 찍는방법
handler2 = logging.FileHandler('my-log.log') # 파일에 로그를 찍는방법
handler1.setFormatter(formatter) # 포멧터 등록
handler2.setFormatter(formatter) # 포멧터 등록
logger.addHandler(handler1) # 로거에 핸들러 추가5
logger.addHandler(handler2) # 로거에 핸들러 추가5

# 기본 핸들러 제거
# logger.propagate = False

# 로그 옵션 동적 처리
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--log-level', choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default = 'INFO', help = '로그 레벨 설정')
args = parser.parse_args()

# 로그 레벨 적용
log_level_args = args.log_level.upper() # upper를 안넣어줘도 됨. 이미 대문자로 넣어져 있기 때문
logger.setLevel(log_level_args)

# 로그 출력하는 방법
# 중요도 1~5, 아래로 갈수록 치명적인 오류
logger.debug('헬로우5') # 5
logger.info('헬로우4') # 4
logger.warning('헬로우3') # 3
logger.error('헬로우2') # 2
logger.critical('헬로우1') # 1

# 디버깅 하는 방법
# flask
# python app.py -d DEBUG / python app.py -d INFO

# CURL
# curl 127.0.0.1/loglevel?level=INFO

# 로그 옵션을 처리해주었을 경우엔
# python mylog.py --log-level CRITICAL 