import datetime


def main():
    now = datetime.datetime.now()
    return now.minute * now.hour


print(main())
