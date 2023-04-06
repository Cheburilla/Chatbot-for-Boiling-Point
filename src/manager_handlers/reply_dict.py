# СТРУКТУРА
# 'ключ': [[сообщение1, [[ключи кнопок], кнопки]], [сообщение2, None], [ключ]]


reply_dict = {'yes': [['Вы организатор или участник?', [['organizer', 'participant', 'user'], "Организатор", "Участник", "Просто интересуюсь"]]],
              'no': [["Для посещения Точки кипения вам необходимо зарегистрироваться на платформе Leader\-ID\."
                        " Без этого вы не сможете организовывать мероприятия и участвовать в них\.\n\nLeader\-ID – цифровая"
                        " среда Точек кипения, библиотека мероприятий и активностей\. Leader\-ID помогает лидерам\, "
                        "командам\, студентам и сообществам подниматься на новый уровень карьерного\, "
                        "профессионального и личностного роста\.\n\nДля регистрации вам необходимо указать номер "
                        "телефона или создать аккаунт через соцсети \: ВКонтакте\, Яндекс\, Телеграм\, Гугл\.", None],
                     ['yes']],
            'organizer': [['Бронировали ли Вы или регистрировали своё мероприятие\?', [['dont_book', 'reg_yes', 'reg_check'],
                                                                                         "Я не бронировал(а) и не регистрировал(а)", "Я бронировал(а), но не регистрировал(а)", "Я регистрировал(а) мероприятие"]]],
            'user': [['Вы можете задать мне любые вопросы\, связанные с Точкой кипения ОмГТУ\, ведь я \- интеллектуальный чат\-бот🤖🐱'
                        '\n\nЕсли вы не знаете\, как сформулировать ваш вопрос\, используйте примеры\:\n\- Как зарегистрировать мероприятие\?'
                        '\n\- Как попасть в Точку кипения?\n\- Как проверить\, что меня отметили на мероприятии\?\n\- Частые вопросы'
                        '\n\- Когда пройдёт модерация моего мероприятия\?\n\- Забронировать мероприятие\n\- Что такое команда\, и как её создать\?'
                        '\n\- Как принять участие в мероприятии\?', None]],
            'participant': [['Что вас интересует\?', [['how_to_participate', 'how_to_get', 'faq'], 'Как принять участие в мероприятии?', 'Как попасть в Точку кипения?', 'Частые вопросы']]],
            'dont_book': [['Хотите ли вы забронировать ваше мероприятие\?\n\nОбратите внимание\, что бронь является предварительной'
                         '\, и для того, чтобы провести мероприятие\, вам необходимо зарегистрировать его\.', [['book_yes', 'reg_yes'], 'Да', 'Нет']]],
            'book_yes': [['Процесс бронирования', None], ['Знаете ли вы\, как правильно регистрировать и оформлять мероприятие на Leader\-ID\?',
                        [['reg_yes', 'user'], 'Не знаю', 'Знаю']]],
            'reg_yes': [['Инструкция по регистрации мероприятия', None], ['user']],
            'reg_check': [['❗Важный момент❗\nУбедитесь в том\, что ваше мероприятие имеет подобающий вид\:\n\- в мероприятии на Leader\-ID указаны все спикеры ' \
                        'и приглашённые гости\n\- у мероприятия есть баннер\, отображающий его суть\n\- описание мероприятие отформатировано так\, что его легко читать\, ' \
                        'а также использованы все необходимые инструменты форматирования\n\- перечислено всё необходимое оборудование\(с учётом того\, что ' \
                        'предоставляемая техника ограничена\)', None], ['moder'], ['user']],
            'moder': [['Когда моё мероприятие отмодерируют\?\nПроверьте\, что место мероприятия указано верно\: \"Точка кипения ОмГТУ\"\n\nУчтите\, что модерация в ' \
                        'рабочие дни занимает около 12 часов\. Если ваше мероприятие создано и оформлено корректно\, администраторы в ближайшее время рассмотрят вашу заявку\.', None]],
            'how_to_participate': [['Инструкция по участию в мероприятии', None], ['user']],
            'how_to_get': [['🏠Адрес университетской Точки кипения\: Проспект Мира\, 11к6\n\n🕒Часы работы Точки\: \.\.\:\.\. \- \.\.\:\.\.\n\nТочка находится в 6\-ом корпусе ' \
                        'ОмГТУ\, вход в будние дни осуществляется через 6\-ой корпус\, главный корпус или столовую\, в воскресенье только через главный\.', None],
                        ['user']],
            'faq': [['Частые вопросы\:', [['team', 'rules', 'why', 'error', 'ev_check'], 'Что такое команда и как её создать?', 'Правила Точки кипения', 'Зачем нужен Leader-ID?', 'Некорректная работа сайта', 'Как проверить, что меня отметили на мероприятии?']]],
            'team': [['Инструкция по созданию команды', None], ['user']],
            'rules': [['⚖️Правила проведения мероприятий\:\n🚭Не курить\n🍺Не распивать спиртные напитки\n🥪Много кушать не надо\n\n🚫Запрещены мероприятия\:\nПолитические\nРекламные\nПлатные', None], ['user']],
            'why': [['Профиль на Leader\-ID — это возможность присоединиться к миллионам предпринимателей\, исследователей\, студентов и волонтеров\, чтобы ' \
                        'получить доступ к Точкам кипения по всей стране и десяткам мероприятий каждый день\. Учитесь у лучших\, собирайте команду\, ' \
                        'вливайтесь в высокотехнологичные стартапы и привлекайте инвесторов — все это здесь есть\.', None], ['user']],
            'error': [['Попробуйте обновить ваш веб браузер и почистить cookie файлы для нашего сайта. В большинстве случаев это помогает решить проблему.' \
                       '\n\n🍪Cookie файлы\:\nGoogle Chrome — chrome\:\/\/settings\/siteData\?searchSubpage\=leader\-id\.ru\nЯндекс\.Браузер — browser\:\/\/settings\/siteData' \
                        '\nFireFox — about\:preferences\#privacy \(далее откройте «Куки и данные» \> «Управление данными»\)\nMicrosoft Edge — edge\:\/\/settings' \
                        '\/cookies\/detail\?site\=leader\-id\.ru', None], ['user']],
            'ev_check': [['К сожалению\, на данный момент проверить свою отметку на мероприятии нельзя\. Однако разработчики уже работают над этой проблемой⚙️🔧', None], ['user']]}
