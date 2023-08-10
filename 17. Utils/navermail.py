import smtplib


smtp = smtplib.SMTP_SSL('smtp.naver.com', 465)

smtp.ehlo()

naver_pw = open('secret.txt', 'r').read() 
smtp.login('www.naver.com', naver_pw)

from email.message import EmailMessage # 이메일 본문을 만드는 라이브러리
msg = EmailMessage()

msg['Subject'] = '메일제목'
msg['FROM'] = 'sender@naver.com'
msg['To'] = 'receiver@naver.com'
msg.set_content('메일 본문, 멀티라인도 가능, 여기에 각자 쓰고 싶은 메시지 작성')

smtp.send_message(msg)

smtp.quit()