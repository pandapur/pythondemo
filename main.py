import datetime

DATE_FORMAT_GERMAN = '%d.%m.%Y %H:%M:%S'
REMAINING_DAYS_TXT = 'Es verbleiben {} Tage'


def get_date():
    date = datetime.datetime.now()
    return date.strftime(DATE_FORMAT_GERMAN)


def get_remaining_days():
    day_of_year = datetime.datetime.now().strftime('%j')
    return 365 - int(day_of_year)


if __name__ == '__main__':
    print(get_date())
    print(REMAINING_DAYS_TXT.format(get_remaining_days()))
