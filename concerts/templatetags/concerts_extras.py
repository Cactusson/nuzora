from django import template


register = template.Library()

months_dict = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря',
    }


@register.filter(name="translate_date")
def translate_date(date):
    year = date.year
    month = date.month
    day = date.day
    return '{} {} {}'.format(day, months_dict[month], year)


@register.filter(name="number_of_concerts")
def number_of_concerts(number):
    word = 'концерт'
    end = ''
    number = str(number)
    if number[-1] == '1':
        if len(number) > 1:
            if number[-2] == '1':
                end = 'ов'
    elif number[-1] in ['2', '3', '4']:
        if len(number) > 1:
            if number[-2] == '1':
                end = 'ов'
            else:
                end = 'а'
        else:
            end = 'а'
    else:
        end = 'ов'
    return number + ' ' + word + end
