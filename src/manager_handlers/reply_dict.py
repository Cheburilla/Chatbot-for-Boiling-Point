# СТРУКТУРА
# 'ключ': [[сообщение1, [[ключи кнопок], кнопки], [ссылка на фото]], [сообщение2, None, None], [ключ]]


reply_dict = {'yes': [['Вы организатор или участник?', [['organizer', 'participant', 'user'], "Организатор", "Участник", "Просто интересуюсь"], None]],
              'no': [["Для посещения Точки кипения вам необходимо зарегистрироваться на платформе Leader\-ID\."
                        " Без этого вы не сможете организовывать мероприятия и участвовать в них\.\n\nLeader\-ID – цифровая"
                        " среда Точек кипения, библиотека мероприятий и активностей\. Leader\-ID помогает лидерам\, "
                        "командам\, студентам и сообществам подниматься на новый уровень карьерного\, "
                        "профессионального и личностного роста\.\n\nДля регистрации вам необходимо указать номер "
                        "телефона или создать аккаунт через соцсети \: ВКонтакте\, Яндекс\, Телеграм\, Гугл\.", None, None],
                     ['yes']],
            'organizer': [['Бронировали ли Вы или регистрировали своё мероприятие\?', [['dont_book', 'reg_yes', 'reg_check'],
                                                                                         "Я не бронировал(а) и не регистрировал(а)", "Я бронировал(а), но не регистрировал(а)", "Я регистрировал(а) мероприятие"], None]],
            'user': [['Вы можете задать мне любые вопросы\, связанные с Точкой кипения ОмГТУ\, ведь я \- интеллектуальный чат\-бот🤖🐱'
                        '\n\nЕсли вы не знаете\, как сформулировать ваш вопрос\, используйте примеры\:\n\- Как зарегистрировать мероприятие\?'
                        '\n\- Как попасть в Точку кипения?\n\- Как проверить\, что меня отметили на мероприятии\?\n\- Частые вопросы'
                        '\n\- Когда пройдёт модерация моего мероприятия\?\n\- Забронировать мероприятие\n\- Что такое команда\, и как её создать\?'
                        '\n\- Как принять участие в мероприятии\?', None, None]],
            'participant': [['Что вас интересует\?', [['how_to_participate', 'how_to_get', 'faq'], 'Как принять участие в мероприятии?', 'Как попасть в Точку кипения?', 'Частые вопросы'], None]],
            'dont_book': [['Хотите ли вы забронировать ваше мероприятие\?\n\nОбратите внимание\, что бронь является предварительной'
                         '\, и для того, чтобы провести мероприятие\, вам необходимо зарегистрировать его\.', [['book_yes', 'reg_yes'], 'Да', 'Нет'], None]],
            'book_yes': [['Введите команду \/book для того, чтобы начать процесс бронирования', None, None], ['Знаете ли вы\, как правильно регистрировать и оформлять мероприятие на Leader\-ID\?',
                        [['reg_yes', 'user'], 'Не знаю', 'Знаю'], None]],
            'reg_yes': [['Инструкция по регистрации мероприятия', None, None], [None, None, 'https://sun9-77.userapi.com/impg/aGVU03idMQ3fCB4JTKW3g7KYdKDPpbEvRGZlYQ/EC2l_p0ThcA.jpg?size=1595x673&quality=95&sign=db6ef28d43529b9b3a49d69fab75c281&type=album'], [None, None, 'https://sun9-15.userapi.com/impg/MHKJFPQ4xyVb9ttut9SVYZemqVMaNn8VOGHXJA/-XNZ_0WCxis.jpg?size=1615x826&quality=96&sign=77c52672e6dd391fc37f88eaa6def19b&type=album'], [None, None, 'https://sun9-7.userapi.com/impg/e6j8JvATM0eBY1E48Liy6MA96itDe2F63STrSQ/MZClhtMCCY0.jpg?size=1606x715&quality=95&sign=d14a7910d6e6bc82ec4957ef0512ac48&type=album'], [None, None, 'https://sun3-23.userapi.com/impg/jF11tsimGJXmNB_wcJa0f58GJcmfVnqf0Z_0oQ/NsZbNETFXCA.jpg?size=1195x610&quality=95&sign=31bb23339f2873a7347904c3b629b9b9&type=album'], [None, None, 'https://sun9-79.userapi.com/impg/YBPe7ItLyuy_61pn9fHyWqV7TkXSbrQE-uI0TA/7X8EwrZBtjw.jpg?size=1194x853&quality=95&sign=d0760ae99d8586de41d4ca2356fbded8&type=album'], [None, None, 'https://sun9-59.userapi.com/impg/hcaJ9LtFBr0M3E5uQg5o-Zs7AlBHIvtKK0ehJw/cK8CSyQaStM.jpg?size=1191x694&quality=95&sign=f54bba0028d0b320c3c80ab67ab7f75e&type=album'], [None, None, 'https://sun9-33.userapi.com/impg/lGo43y8yDxqXmqblNC47Xd6sFhjO_d0MnZ7Duw/Q6dl-wamuxU.jpg?size=948x884&quality=95&sign=4e4801461b4c9fccb8ef5e94303c3b5b&type=album'], [None, None, 'https://sun9-6.userapi.com/impg/odEo7qKL96Yb6_0wo_a4mgWgdrKPLLhr79rRTQ/y3auRFrB0qc.jpg?size=1066x805&quality=95&sign=3ece4841f74b1929950bb4df98eb0ec8&type=album'], [None, None, 'https://sun9-72.userapi.com/impg/-XwmlgmCD8IwdWLpFpKjwbn7GGY-jk5xbdvxtQ/CA82xFZm_DE.jpg?size=1073x363&quality=95&sign=0579dd5f369539035840d7658c5042d5&type=album'], [None, None, 'https://sun9-12.userapi.com/impg/YONgovItPsrALDVjY8l8y3PLuyl_H1vI20IceA/W-7DbNLHIcA.jpg?size=1209x818&quality=95&sign=89728c52f120f548d7092d059492a037&type=album'], [None, None, 'https://sun9-77.userapi.com/impg/Pw_cXEnb6ct0s4PjgScf8pQ79r6Sua0XocxL0Q/9tLdioPCkAM.jpg?size=1130x837&quality=95&sign=20bde0bfd720ec94cb45fe0c26029912&type=album'], [None, None, 'https://sun9-80.userapi.com/impg/oNDw_yMJp-v_O8fbRLgGiXfTl0gryAn4L0AytQ/dgeAaVsRdJA.jpg?size=1135x702&quality=95&sign=e3e1cc59b17b63c0f8cb6609a3696c12&type=album'], [None, None, 'https://sun9-70.userapi.com/impg/LrorPi-4kGTDE0PC1c-JUgy2_nXjiBJmqkKNeA/a_gY0FHsmac.jpg?size=1210x483&quality=95&sign=64f7ed9d31f931a721178140dc92a634&type=album'], [None, None, 'https://sun9-79.userapi.com/impg/exzJe1C6Tuj_CKjt1ojp_96WMy6jXz0fPibx4Q/a-CfkcWV6V0.jpg?size=1086x852&quality=95&sign=d8fde1bdb63fea1a130e1a2f20f90af1&type=album'], [None, None, 'https://sun9-6.userapi.com/impg/MJCWg7rMpAzHQIxD2sspEuY1xD4Vxig6n61efw/dhX-o5K-4SU.jpg?size=1210x562&quality=95&sign=de761ff7731158bb1b481968295a294b&type=album'], [None, None, 'https://sun9-77.userapi.com/impg/CEZyRSzuxQHz2Oyg3Ke-_uaIp54Xk2xIuAa0fg/pOHNjhWIJjs.jpg?size=1229x232&quality=95&sign=12584667d9ec199a6018ea27d6c45204&type=album'], ['user']],
            'reg_check': [['❗Важный момент❗\nУбедитесь в том\, что ваше мероприятие имеет подобающий вид\:\n\- в мероприятии на Leader\-ID указаны все спикеры ' \
                        'и приглашённые гости\n\- у мероприятия есть баннер\, отображающий его суть\n\- описание мероприятие отформатировано так\, что его легко читать\, ' \
                        'а также использованы все необходимые инструменты форматирования\n\- перечислено всё необходимое оборудование\(с учётом того\, что ' \
                        'предоставляемая техника ограничена\)', None, None], ['moder'], ['user']],
            'moder': [['Когда моё мероприятие отмодерируют\?\nПроверьте\, что место мероприятия указано верно\: \"Точка кипения ОмГТУ\"\n\nУчтите\, что модерация в ' \
                        'рабочие дни занимает около 12 часов\. Если ваше мероприятие создано и оформлено корректно\, администраторы в ближайшее время рассмотрят вашу заявку\.', None, None]],
            'how_to_participate': [['Инструкция по участию в мероприятии', None, None], ['user']],
            'how_to_get': [['🏠Адрес университетской Точки кипения\: Проспект Мира\, 11к6\n\n🕒Часы работы Точки\: \.\.\:\.\. \- \.\.\:\.\.\n\nТочка находится в 6\-ом корпусе ' \
                        'ОмГТУ\, вход в будние дни осуществляется через 6\-ой корпус\, главный корпус или столовую\, в воскресенье только через главный\.', None, None],
                        ['user']],
            'faq': [['Частые вопросы\:', [['team', 'rules', 'why', 'error', 'ev_check'], 'Что такое команда и как её создать?', 'Правила Точки кипения', 'Зачем нужен Leader-ID?', 'Некорректная работа сайта', 'Как проверить, что меня отметили на мероприятии?'], None]],
            'team': [['Инструкция по созданию команды', None, None], ['user']],
            'rules': [['⚖️Правила проведения мероприятий\:\n🚭Не курить\n🍺Не распивать спиртные напитки\n🥪Много кушать не надо\n\n🚫Запрещены мероприятия\:\nПолитические\nРекламные\nПлатные', None, None], ['user']],
            'why': [['Профиль на Leader\-ID — это возможность присоединиться к миллионам предпринимателей\, исследователей\, студентов и волонтеров\, чтобы ' \
                        'получить доступ к Точкам кипения по всей стране и десяткам мероприятий каждый день\. Учитесь у лучших\, собирайте команду\, ' \
                        'вливайтесь в высокотехнологичные стартапы и привлекайте инвесторов — все это здесь есть\.', None, None], ['user']],
            'error': [['Попробуйте обновить ваш веб браузер и почистить cookie файлы для нашего сайта. В большинстве случаев это помогает решить проблему.' \
                       '\n\n🍪Cookie файлы\:\nGoogle Chrome — chrome\:\/\/settings\/siteData\?searchSubpage\=leader\-id\.ru\nЯндекс\.Браузер — browser\:\/\/settings\/siteData' \
                        '\nFireFox — about\:preferences\#privacy \(далее откройте «Куки и данные» \> «Управление данными»\)\nMicrosoft Edge — edge\:\/\/settings' \
                        '\/cookies\/detail\?site\=leader\-id\.ru', None, None], ['user']],
            'ev_check': [['К сожалению\, на данный момент проверить свою отметку на мероприятии нельзя\. Однако разработчики уже работают над этой проблемой⚙️🔧', None, None], ['user']]}
