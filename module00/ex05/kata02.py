import datetime


# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

if __name__ == '__main__':
    date = datetime.datetime(*kata)
    s = date.strftime('%m/%d/%Y %H:%M')
    print(s)
