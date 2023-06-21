# 사용자로부터 점수를 입력받는다
# 사용자로부터 이름을 입력받는다
# 이 점수가 최고점수면 하이스코어를 기록한다
# 'high'라고 입력하면 현재까지의 하이스코어와 그 사람이 누군지 출력한다.
# 'history'라고 입력하면 그동안 입력한 모든 점수와 사람을 출력한다

# ------------------------
# 전역 변수
# ------------------------
game_history = []
highscore = 0

# ------------------------
# 각종 함수
# ------------------------
def input_score():
    score = int(input('점수:'))
    name = input('이름:')

    return score, name


def store_result(score, name):
    global highscore

    game_score = (score, name) # 튜플
    game_history.append(game_score)
    if(score>highscore):
        highscore=score

def print_history():
    print('----------')
    print('(점수, 이름)')
    print('----------')
    print(game_history)

def print_highscore():
    # for score,_ in highscore:
    #     print(score)
    #     if score > highscore:
    #         highscore = score
    
    print('최고점수:',highscore)
    



def input_mode():
    mode_ops =['score','history','high']
    mode = input('입력모드:')
    if mode not in mode_ops:
        mode = input('입력모드:')

    return mode

# ------------------------
# 메인 함수
# ------------------------
if __name__ == '__main__': # 메인함수 정의
    def main():
        while True:
            op = input_mode()
            if op == 'score':
                score, name = input_score()
                store_result(score, name)
            elif op == 'history':
                print_history()
            elif op == 'high':
                print_highscore()

main()