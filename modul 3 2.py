def send_email(message, recipient,*,sender='university.help@gmail.com'):
    recipient=str(recipient)
    sender=str(sender)
    r=recipient.find('@')
    r1=recipient.find('.com')
    r2=recipient.find('.ru')
    r3=recipient.find('.net')
    s=sender.find('@')
    s1=sender.find('.com')
    s2=sender.find('.ru')
    s3=sender.find('.net')
    if r==-1 or s==-1:
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    if r1==-1 and r2==-1 and r3==-1:
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    elif s1==-1 and s2==-1 and s3==-1:
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    elif sender==recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender=='university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', recipient, 'на адрес ', sender)
    elif sender!='university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ',recipient)
send_email('Это сообщение для проверки связи ', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')