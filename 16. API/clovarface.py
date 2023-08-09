import os
import sys
import requests
import json
import cv2

def clova_face(filename):
    client_id = "sInGF4qWfuda2Nztl_2K"
    client_secret = open('secret.txt', 'r').read()
    url = "https://openapi.naver.com/v1/vision/face"  # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)
    
    data = json.loads(response.text)
    return data

def my_opencv(filename):
    face_info = clova_face(filename)
    # print(face_info)
    image = cv2.imread(filename)

    for face in face_info['faces']:
        roi = face['roi']
        x, y, w, h = roi['x'], roi['y'], roi['width'], roi['height']
        print(x,y,w,h)

        gender = face['gender']['value']
        age = face['age']['value']
        emotion = face['emotion']['value']

        cv2.rectangle(image, (x,y), (x + w,y + h), (0,0,255),3 ) # 사각형 그리기
        cv2.putText(image, gender, (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 3) # 글자 삽입
        cv2.putText(image, age, (x+150,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 3) 
        cv2.putText(image, emotion, (x+300,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 3) 

        # 나이, 감정

    cv2.imshow('Window Name', image) # 파일 읽어오기 / 첫번째인자: 윈도우창 이름 설정, 두번째인자: 이미지 주소
    cv2.waitKey(0) # 키보드의 입력을 받게 기다리게 함.

if __name__ == '__main__':
    filename = 'images/김채원.jpeg'
    my_opencv(filename)