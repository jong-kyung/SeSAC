const input = document.querySelector('input')
const buttons = document.querySelectorAll('button')
const operator = ['+', '-', '*', '/']
let result = 0;
let number = '';

buttons.forEach((a, i) => {
    a.addEventListener('click', (e) => {
        let _this = e.currentTarget;
        if (_this.innerHTML == 'C') {
            /* 사용자의 UI 초기화 및 입력중이었던 값 초기화 */
            number = '';
            input.value = '';
            result = 0;
        } else if (_this.innerHTML == '=') {
        

            input.value = result
        } else { // 숫자를 눌렀을 경우
            number += _this.innerHTML
            input.value = number
        }
    })
})
