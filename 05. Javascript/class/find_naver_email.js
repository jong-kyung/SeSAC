// 네이버 이메일 콘솔창에서 자동으로 체크하는 기능
const user = document.querySelectorAll('.button_sender')
let email = [];
user.forEach((a, i) => {
    if (a.getAttribute('title').includes('emart.com')) {
        email.push(a.parentElement.parentElement.parentElement)
        email.forEach((a,i)=>{
            a.className = 'mail_item selected mail-5010'
            a.firstElementChild.firstElementChild.firstElementChild.checked = true
        })
    }
})