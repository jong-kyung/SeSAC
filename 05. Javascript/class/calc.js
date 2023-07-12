const input = document.querySelector('input')
const buttons = document.querySelectorAll('button')
const operator = ['+', '-', '*', '/']
let result = 0;
let number = '';
let user_request = []

buttons.forEach((a, i) => {
    a.className = 'btn btn-light'
    
    a.addEventListener('click', (e) => {
        let _this = e.currentTarget;
        if (operator.includes(_this.innerHTML)) { // 연산자가 있는지 확인
            if (number != '') { // 연산자를 먼저 눌렀을때 0으로 입력되는 것 방지
                user_request.push(Number(number))
            }

            /* 사용자의 UI 초기화 및 입력중이었던 값 초기화 */
            number = '';
            input.value = '';

            /* 어레이에 연산자 추가 */
            if (operator.includes(user_request[1])) { // 이미 연산자가 있을때
                user_request.pop() // 두번 누를경우 입력되는 0을 제거 하기위함
            } else if (user_request.length === 1) { // 앞에 입력된 값이 있을때만 연산자 추가
                user_request.push(_this.innerHTML);
            }

        } else if (_this.innerHTML == 'C') {
            /* 사용자의 UI 초기화 및 입력중이었던 값 초기화 */
            number = '';
            user_request = [];
            input.value = '';
            result = 0;
        } else if (_this.innerHTML == '=') {
            user_request.push(Number(number)) // 입력된 숫자를 어레이에 넣음

            /* 계산로직 */
            if (user_request[1] == operator[0]) {
                result = user_request[0] + user_request[2]
            } else if (user_request[1] == operator[1]) {
                result = user_request[0] - user_request[2]
            } else if (user_request[1] == operator[2]) {
                result = user_request[0] * user_request[2]
            } else if (user_request[1] == operator[3]) {
                if (user_request[2] == 0) {
                    result = '오류'
                    user_request = []
                } else {
                    result = user_request[0] / user_request[2]
                }
            }
            input.value = result
            number = ''
            user_request = []
            user_request.push(result)
        } else { // 숫자를 눌렀을 경우
            number += _this.innerHTML
            input.value = number
        }
    })
})
