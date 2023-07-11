const input = document.querySelector('input')
const buttons = document.querySelectorAll('button')
const operator = ['+', '-', '*', '/']
let number = '';

buttons.forEach((a, i) => {
    a.addEventListener('click', (e) => {
        let _this = e.currentTarget;
        if (operator.includes(_this.innerHTML)) {
            input.value = '';
        } else if (_this.innerHTML == 'C') {
            /* 사용자의 UI 초기화 */
            input.value = '';
            number = '';
        } else if (_this.innerHTML == '=') {
            input.value = eval(number)
        } else { // 숫자를 눌렀을 경우
            number += _this.innerHTML
            input.value = number
        }
    })
})
