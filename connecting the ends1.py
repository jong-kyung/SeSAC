words = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']

first_word = '기차'
print('끝말잇기를 하자. 내가 먼저 말할게.' + first_word)
spoken_words = [first_word]

while len(words) >0:
    user_input = input('> ')
    
    if not user_input: # user_input이 없는 경우
        continue
    elif user_input == "졌다": 
        print('내가 이김')
        break
    elif user_input[0] != spoken_words[-1][-1]: # 파이썬에선 [-1] 인덱싱을 통해 가장 마지막 요소에 접근함
        print('글자가 안 이어져. 내가 이겼다!')
        break
    elif user_input in spoken_words:
        print('아까 했던 말이야. 내가 이겼어!')
        break
    else:
        spoken_words.append(user_input)
        my_word = ''
        for word in list(set(words) - set(first_word)):
            if word[0] == user_input[-1]:
                my_word = word
                break
       
        if not my_word:
            print('모르겠다. 내가 졌어.')
            break
        else:
            print(my_word)
            spoken_words.append(my_word)
            continue