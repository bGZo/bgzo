# author: @bGZoCg
# update: 2022/2/8
# More social medias here:
# https://twitter.com/decade_progress
# https://twitter.com/year_progress

from datetime import date

HEARDER = '''\
![](https://komarev.com/ghpvc/?username=bGZoCg) <img src="https://img.shields.io/github/last-commit/bgzo/blog?color=ff69b4&label=blog%20update%20%40%20"/> 

<img align="right" width="30%" src="https://media.giphy.com/media/k8kITi9SAwe9JWbUaH/giphy.gif">

## Progress Bar
'''

PROFILE='''\
## What About Me?

```diff
@@ IMU STU @@
# 📖 major in Software Engineering
! 🤔 keeping individual thinking
- 💻 insisting to push log daily and coding  
+ 🎯 diversity is essential to happiness
```

- [2021](https://github.com/bGZoCg/2021)
'''


def days_in_year(year):
    if is_year_leap(year):
        return 366
    return 365

def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30

def days_till_now():
    days = 0
    today = date.today()
    for i in range(1, today.month):
        days += days_in_month(today.year, i)
    days += today.day
    return days

def draw_year_progress_bar():
    tmp = ' Year Passed '
    days = days_till_now()
    for i in range(0, round(days*15/days_in_year(date.today().year))):
        tmp += "▓"
    for i in range(round(days*15/days_in_year(date.today().year)), 15):
        tmp += "░"
    tmp += ' ' + str(round(days_till_now()/days_in_year(date.today().year)*100, 2)) + '%'
    return tmp

def draw_month_progress_bar():
    tmp = 'Month Passed '
    days = date.today().day
    for i in range(0, round(days/2)):
        tmp += "▓"
    for i in range(round(days/2), 15):
        tmp += "░"
    tmp += ' ' + str(round(days*100/days_in_month(date.today().year, date.today().month))) + '%'
    return tmp

def write_file():
    with open('progress.txt', 'w') as f:
        f.write(str(date.today()))

def main():
    progress = HEARDER + '\n' + '```\n' +  draw_year_progress_bar() + '\n\n' + draw_month_progress_bar() + '\n' + '```\n'+ PROFILE
    print(progress)

main()
