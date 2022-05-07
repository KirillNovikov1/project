import os

from flask import Flask, request
import logging
import json
import random

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

zz = ['Показать информацию', 'Показать случайный факт', 'Пока']

aquarius = {'facts': ['Думаете - "сложно сказать...", Говорите - лучше не говорите, Делаете - лучше всех',
                      "Постоянен в своих убеждениях и желаниях", "Факт: Вы сликшом вызываетесь к людям",
                      'Водолей будет уверен в своей правоте до самого конца', 'Не любите критику в свой адрес'],
            'info': ['Знак Зодиака: Водолей', 'Стихия: Воздух', 'Качество: фиксированное', 'Цвет: светло-голубой,\
                     серебристый', 'День: суббота', 'Правитель: Уран, Сатурн', 'Наибольшая общая совместимость: Лев,\
                      Стрелец', 'Счастливые числа: 4, 7, 11, 22, 29',
                     'Диапазон дат: 20 января — 18 февраля']}  # водолей

pisces = {'facts': ['Думаете - странно, Говорите - по-своему, Делаете - не себе, не людям', 'Вас мало кто понимает',
                    'Не хвастаются своими успехами, хотя достижений у них хватает', 'Вы постоянно стоите перед выбором',
                    'Рыбы не делят людей на плохих и хороших, потому готовы помогать любому'],
          'info': ['Знак Зодиака: Рыбы', 'Стихия: Вода', 'Качество: мутабельное', 'Цвет: лиловый, сиреневый,\
                    фиолетовый, морской, зеленый', 'День: четверг', 'Правитель: Нептун, Юпитер',
                   'Наибольшая общая совместимость: Дева, Телец', 'Счастливые числа: 3, 9, 12, 15, 18, 24',
                   'Диапазон дат: 19 февраля — 20 марта']}  # рыбы

aries = {'facts': ['Думаете - много, Говорите - мало, Делаете - хорошо', 'Звезды наделили вас храбростью и добротой',
                   'Вы вряд-ли умеете хорошо лгать в близи незнакомых людей',
                   "Вы очень доверычивы и зависите от других",
                   'Вы не умеет лгать и поэтому ваш страх - быть обманутым'],
         'info': ['Знак Зодиака: Овен', 'Стихия: Огонь', 'Качество: кардинальное', 'Цвет: красный', 'День: вторник',
                  'Правитель: Марс', 'Наибольшая общая совместимость: Весы, Лев', 'Счастливые числа: 1, 8, 17',
                  'Диапазон дат: 21 марта — 19 апреля']}  # овен

taurus = {'facts': ['Думаете - о многом, Говорите - убидетельно, Делаете - как получится',
                    'Вы трудно переживаете любые перемены в жизни', 'Невероятный упрямец - ваше второе имя',
                    'Такие люди как вы умеют, но любят лгать', 'Стремление к высотам - не ваш приоритет'],
          'info': ['Знак Зодиака: Телец', 'Стихия: Земля', 'Качество: фиксированное', 'Цвет: зеленый', 'День: пятница',
                   'Правитель: Венера', 'Наибольшая общая совместимость: Скорпионю, Рак', 'Счастливые числа: 2, 6, 12',
                   'Диапазон дат: 20  апреля — 20 мая']}

gemini = {'facts': ['Думаете - о себе, Говорите - что думаете, Делаете - по вашему мнению хорошо',
                    "Вы энергичны, как никто другой, жизнь бьёт из вас ключом", "Вы не учитесь на своих ошибках",
                    "Не замечали за собой стремление к легкому успеху", "Вы приверженцы своих привычек, непостоянны"],
          'info': ['Знак Зодиака: Близнецы', 'Стихия: Воздух', 'Качество: мутабельное', 'Цвет: салатовый',
                   'День: пятница',
                   'Правитель: Меркурий', 'Наибольшая общая совместимость: Стрелец, Водолей',
                   'Счастливые числа: 5, 7, 23',
                   'Диапазон дат: 21 мая — 20 июня']}

cancer = {'facts': ["Думаете - Постоянно, Говорите - заманчиво, Делаете - что скажут", "Рак - самый таниственный Знак",
                    "Вы лидер с большой буквы, ваше стремление покорять этот мир непостижимо",
                    "Способны видеть людей 'насквозь'",
                    "Вы нацелены на успех, но часто терпите крах"],
          'info': ['Знак Зодиака: Рак', 'Стихия: Вода', 'Качество: кардинальное', 'Цвет: белый', 'День: понедельник',
                   'Правитель: Луна', 'Наибольшая общая совместимость: Козерог, Телец', 'Счастливые числа: 2, 3, 15',
                   'Диапазон дат: 21 июня - 22 июля']}

leo = {'facts': ["Думаете - точно, Говорите - лишнее, Делаете - необходимое",
                 "Авторитетная натура, которая несёт в мир свет",
                 'Львы прекрасно чувствуете себя среди людей, не боитесь быть собой и привлекать внимание',
                 'Вы искренний человек, честны и душевны в своём понимании окружащего общества',
                 'Вы не умеете проигрывать и поэтому действуете всегда на своём максимуме'],
       'info': ['Знак Зодиака: Лев', 'Стихия: Огонь', 'Качество: мутабельное', 'Цвет: желтый', 'День: воскресенье',
                'Правитель: Солнце', 'Наибольшая общая совместимость: Водолей, Близнецы', 'Счастливые числа: 1, 3, 19',
                'Диапазон дат: 23 июля - 22 августа']}

virgo = {'facts': ['Думаете - одно, Говорите - другое, Делаете - лучше остальных',
                   "Девы легко переносят трудности и перемены",
                   'Вы способны подмечать даже малейший нюансы во всём. Из-за этого постоянно пытаетесь совершенствова\
                   ться', 'Этот знак зодиака живёт материальными ценностями, забывая про духовный мир',
                   "Среди Дев много миллионеров"],
         'info': ['Знак Зодиака: Дева', 'Стихия: Земля', 'Качество: мутабельное', 'Цвет: серый', 'День: среда',
                  'Правитель: Меркурий', 'Наибольшая общая совместимость: Рыбы, Рак', 'Счастливые числа: 5, 14, 32',
                  'Диапазон дат: 23 августа - 22 сентября']}

libra = {'facts': ['Думаете -  лишнее, Говорите - правду, Делаете - ответственно', "Наделены стратегическими навыками",
                   'Лгать людям - явно не ваш приоритет по жизни',
                   'По мнению астрологов - это самый ленивы знак зодиака',
                   'Вы отличный мотиватор для других людей и умеете сближаться с интересными личностями'],
         'info': ['Знак Зодиака: Весы', 'Стихия: Воздух', 'Качество: кардинальное', 'Цвет: розовый', 'День: пятница',
                  'Правитель: Венера', 'Наибольшая общая совместимость: Овен, Стрелец', 'Счастливые числа: 5, 15, 24',
                  'Диапазон дат: 23 сентября - 22 октября']}

scorpio = {
    'facts': ['Думаете -  сосредоточенно, Говорите - обо всём, Делаете - Что нравится', 'Скорпион - опасный и надёжный',
              'Вы очень прогрессивный человек и стараетесь быть в "тренде"', 'Этот знак зодиака любит мстить',
              'Отличаетесь прямолинейностью, несмотря на свою скрытность'],
    'info': ['Знак Зодиака: Скорпион', 'Стихия: Вода', 'Качество: фиксированное', 'Цвет: красный', 'День: вторник',
             'Правитель: Плутон', 'Наибольшая общая совместимость: Телец, Рак', 'Счастливые числа: 8, 11, 22',
             'Диапазон дат: 23 октября - 21 ноября']}

sagittarius = {'facts': ['Думаете - только о своём, Говорите - не о себе, Делаете - чужими руками',
                         'Всегда готовы к приключениям, хорошим и плохим', 'Стрелец - верный друг на всю жизнь',
                         "Вы всегда прощаете своих обидчиков и не умеете держать зла на других",
                         'Вас невозможно переспорить', 'Знак зодиака с твердыми принципами и  намерениями'],
               'info': ['Знак Зодиака: Стрелец', 'Стихия: Огонь', 'Качество: мутабельное', 'Цвет: синий',
                        'День: четверг',
                        'Правитель: Сатурн', 'Наибольшая общая совместимость: Овен, Близнецы',
                        'Счастливые числа: 7, 9, 21',
                        'Диапазон дат: 22 ноября - 21 декабря']}

capricorn = {'facts': ['Думаете - что в голову прийдёт, Говорите -  до чего додумаетесь, Делаете - что умеете',
                       'Прямой манипулятор, сильная личность', 'Козерог - оптимист до глубины души',
                       'Вы готовы на многое ради успеха, у вас необъятные амбиции', 'Вы обладаете завидной интуицией',
                       'Этот знак зодиака очень ранимый. За внешним безразличием спрятана очень чувствительная натура'],
             'info': ['Знак Зодиака: Козерог', 'Стихия: Земля', 'Качество: кардинальное', 'Цвет: коричневый',
                      'День: суббота',
                      'Правитель: Сатурн', 'Наибольшая общая совместимость: Телец, Рак', 'Счастливые числа: 8, 13, 22',
                      'Диапазон дат: 22 декабря - 19 января']}

sessionStorage = {}


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info(f'Response: {response!r}')
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']

    if req['session']['new']:
        res['response']['text'] = 'Привет! Назови свое имя!'
        sessionStorage[user_id] = {
            'first_name': None
        }
        return

    if sessionStorage[user_id]['first_name'] is None:
        first_name = get_first_name(req)
        if first_name is None:
            res['response']['text'] = \
                'Не расслышала имя. Повтори, пожалуйста!'
        else:
            sessionStorage[user_id]['first_name'] = first_name
            res['response'][
                'text'] = 'Приятно познакомиться, ' \
                          + first_name.title() \
                          + '. Я - Алиса. Укажи свой день рождения и месяц?'

    else:
        command = req['request']['original_utterance']
        if command.lower() == 'пока':

            response = {'text': ' ',
                        "card": {
                            "type": "BigImage",
                            "image_id": "965417/94a216731937fcaf192d",
                            "title": "Ты это, заходи, если что"}}
            res['response'] = response
            res['response']['end_session'] = True

        elif command.lower() == 'показать информацию':

            if "Водолей" in sessionStorage[user_id]['horoscope']:
                aq = ' '
                for i in range(len(aquarius['info'])):
                    aq += aquarius['info'][i] + '\n'
                    res['response']['text'] = aq

            elif "Рыбы" in sessionStorage[user_id]['horoscope']:
                pis = ' '
                for i in range(len(pisces['info'])):
                    pis += pisces['info'][i] + '\n'
                    res['response']['text'] = pis

            elif "Овен" in sessionStorage[user_id]['horoscope']:
                ar = ' '
                for i in range(len(aries['info'])):
                    ar += aries['info'][i] + '\n'
                    res['response']['text'] = ar

            elif "Телец" in sessionStorage[user_id]['horoscope']:
                ta = ' '
                for i in range(len(taurus['info'])):
                    ta += taurus['info'][i] + '\n'
                    res['response']['text'] = ta

            elif "Близнецы" in sessionStorage[user_id]['horoscope']:
                ge = ' '
                for i in range(len(gemini['info'])):
                    ge += gemini['info'][i] + '\n'
                    res['response']['text'] = ge

            elif "Рак" in sessionStorage[user_id]['horoscope']:
                can = ' '
                for i in range(len(cancer['info'])):
                    can += cancer['info'][i] + '\n'
                    res['response']['text'] = can

            elif "Лев" in sessionStorage[user_id]['horoscope']:
                le = ' '
                for i in range(len(leo['info'])):
                    le += leo['info'][i] + '\n'
                    res['response']['text'] = le

            elif "Дева" in sessionStorage[user_id]['horoscope']:
                vr = ' '
                for i in range(len(virgo['info'])):
                    vr += virgo['info'][i] + '\n'
                    res['response']['text'] = vr

            elif "Весы" in sessionStorage[user_id]['horoscope']:
                lib = ' '
                for i in range(len(libra['info'])):
                    lib += libra['info'][i] + '\n'
                    res['response']['text'] = lib

            elif "Скорпион" in sessionStorage[user_id]['horoscope']:
                scr = ' '
                for i in range(len(scorpio['info'])):
                    scr += scorpio['info'][i] + '\n'
                    res['response']['text'] = scr

            elif "Стрелец" in sessionStorage[user_id]['horoscope']:
                sgt = ' '
                for i in range(len(sagittarius['info'])):
                    sgt += sagittarius['info'][i] + '\n'
                    res['response']['text'] = sgt

            elif "Козерог" in sessionStorage[user_id]['horoscope']:
                cpr = ' '
                for i in range(len(capricorn['info'])):
                    cpr += capricorn['info'][i] + '\n'
                    res['response']['text'] = cpr
            else:
                res['response']['text'] = 'Ай-яй-яй, введите дату'

        elif command.lower() == 'показать случайный факт':
            if "Водолей" in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(aquarius['facts'])

            elif 'Рыбы' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(pisces['facts'])

            elif 'Овен' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(aries['facts'])

            elif 'Телец' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(taurus['facts'])

            elif 'Близнецы' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(gemini['facts'])

            elif 'Рак' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(cancer['facts'])

            elif 'Лев' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(leo['facts'])

            elif 'Дева' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(virgo['facts'])

            elif 'Весы' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(libra['facts'])

            elif 'Скорпион' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(scorpio['facts'])

            elif 'Стрелец' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(sagittarius['facts'])

            elif 'Козерог' in sessionStorage[user_id]['horoscope']:
                res['response']['text'] = random.choice(capricorn['facts'])
            else:
                res['response']['text'] = 'Ай-яй-яй, введите дату'

        else:
            day = get_day(req)
            month = get_month(req)

            if day is not None and month is not None:
                if (day >= 23 and month == 12) or (day <= 20 and month == 1):
                    response = {'text': 'Ваш знак зодиака - Козерог',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "997614/1e5e31b7fe32d9048bd5",
                                    "title": "Ваш знак зодиака - Козерог",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-vesov/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 21 and month == 1) or (day <= 19 and month == 2):
                    response = {'text': 'Ваш знак зодиака - Водолей',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1533899/b3fc36aae4d49166f00b",
                                    "title": "Ваш знак зодиака - Водолей",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vodolej/istorija-vodoleja/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 20 and month == 2) or (day <= 20 and month == 3):
                    response = {'text': 'Ваш знак зодиака - Рыбы',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1540737/5ee94ad2a58d910d1631",
                                    "title": "Ваш знак зодиака - Рыбы",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-ryb/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 21 and month == 3) or (day <= 20 and month == 4):
                    response = {'text': 'Ваш знак зодиака - Овен',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "997614/4a01ca30c86a330f72b4",
                                    "title": "Ваш знак зодиака - Овен",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-ovna/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
                    response = {'text': 'Ваш знак зодиака - Телец',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1030494/43e71359701baa44880b",
                                    "title": "Ваш знак зодиака - Телец",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-telca/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
                    response = {'text': 'Ваш знак зодиака - Близнецы',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1652229/7cc7a5f2e77b5b9918c7",
                                    "title": "Ваш знак зодиака - Близнецы",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-bliznecov/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
                    response = {'text': 'Ваш знак зодиака - Рак',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1652229/93d1c9b4ffe5ba7e4d7f",
                                    "title": "Ваш знак зодиака - Рак",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-raka/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 23 and month == 7) or (day <= 21 and month == 8):
                    response = {'text': 'Ваш знак зодиака - Лев',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1652229/119ffec186b55c300dfb",
                                    "title": "Ваш знак зодиака - Лев",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-lva/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 22 and month == 8) or (day <= 23 and month == 9):
                    response = {'text': 'Ваш знак зодиака - Дева',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1521359/254274e4a041ee3e3b03",
                                    "title": "Ваш знак зодиака - Дева",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-devy/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
                    response = {'text': 'Ваш знак зодиака - Весы',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "997614/3f8be4c2173b0f7f3cc1",
                                    "title": "Ваш знак зодиака - Весы",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-vesov/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 24 and month == 10) or (day <= 22 and month == 11):
                    response = {'text': 'Ваш знак зодиака - Скорпион',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "997614/8be52db64acad155052d",
                                    "title": "Ваш знак зодиака - Скорпион",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-scorpiona/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                elif (day >= 23 and month == 11) or (day <= 22 and month == 12):
                    response = {'text': 'Ваш знак зодиака - Стрелец',
                                "card": {
                                    "type": "BigImage",
                                    "image_id": "1652229/75c6dcc81cc52e5e18e8",
                                    "title": "Ваш знак зодиака - Стрелец",
                                    "description": "Нажимая на картинку, вы получаете информацию о знаке",
                                    "button": {
                                        "text": "История знака",
                                        "url": "https://znakizodiaka.info/znakizodiaka/vesy/istorija-strelca/",
                                        "payload": {}
                                    }
                                }
                                }
                    res['response'] = response

                else:
                    res['response']['text'] = 'Введите верное значение'
            else:
                res['response']['text'] = 'Введите верное значение'
            sessionStorage[user_id]['horoscope'] = res['response']['text']
        res['response']['buttons'] = [{'title': znak.title(), 'hide': True} for znak in zz]


def get_day(req):
    for entity in req['request']['nlu']['entities']:
        if entity['type'] == 'YANDEX.DATETIME':
            return entity['value'].get('day')


def get_month(req):
    for entity in req['request']['nlu']['entities']:
        if entity['type'] == 'YANDEX.DATETIME':
            return entity['value'].get('month')


def get_first_name(req):
    for entity in req['request']['nlu']['entities']:
        if entity['type'] == 'YANDEX.FIO':
            return entity['value'].get('first_name', None)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
