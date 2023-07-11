const input = document.querySelector('input')
const buttons = document.querySelectorAll('button')
const operator = ['+', '-', '*', '/']
let result = 0;
let number = '';
let user_request = []

buttons.forEach((a, i) => {
    a.addEventListener('click', (e) => {
        let _this = e.currentTarget;
        console.log(user_request)
        if (operator.includes(_this.innerHTML)) { // 연산자가 있는지 확인
            user_request.push(Number(number))

            /* 사용자의 UI 초기화 및 입력중이었던 값 초기화 */
            number = '';
            input.value = '';

            /* 어레이에 연산자 추가 */
            if (operator.includes(user_request[1])) {
                user_request.pop()
            } else if (user_request.length === 1) {
                if (user_request[0] == 0) {
                    user_request.pop()
                } else {
                    user_request.push(_this.innerHTML);
                }
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
                result = user_request[0] / user_request[2]
            }
            input.value = result
        } else { // 숫자를 눌렀을 경우
            number += _this.innerHTML
            input.value = number
        }
    })
})
