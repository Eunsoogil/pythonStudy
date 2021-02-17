# built_in module이 있음
# email.py로 명명하면 오류남

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path와 비슷

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Eunsoo Gil'
email['to'] = '123@naver.com'  # 보낼 이메일
email['subject'] = 'work'

email.set_content(html.substitute({'name': 'eunsoo', 'age': 11}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # smtp 서버 구동 명령어
    smtp.starttls()  # secure
    smtp.login('email@gmail.com', '1234')  # 이메일, 비밀번호 입력
    smtp.send_message(email)
    print('success')
