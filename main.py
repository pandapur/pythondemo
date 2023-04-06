import datetime

DATE_FORMAT_GERMAN = '%d.%m.%Y %H:%M:%S'


def get_date():
    date = datetime.datetime.now()
    return date.strftime(DATE_FORMAT_GERMAN)


if __name__ == '__main__':
    print(get_date())
