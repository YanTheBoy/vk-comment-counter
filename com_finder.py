import requests
from datetime import datetime, timedelta, time
import plotly.graph_objects as go


def get_number_of_comments_by_day():
    total_comms_per_day = []
    date_time = get_time_intervals_for_last_7_days()
    day = 0   # first day of the week
    while day != len(date_time):
        page_offset = 0
        url = 'https://api.vk.com/method/'
        params = {
            'access_token': '8906a95d8906a95d8906a95d62896dcd4d889068906a95dd411d85760beadc00db1139d',
            'v': '5.103',
            'q': 'Coca-cola',
            'start_time': date_time[day][1],
            'end_time': date_time[day][0],
            'count': 200,
            'start_from': page_offset
        }
        method = 'newsfeed.search'
        response = requests.get(url+method, params=params).json()
        num_comments_per_day = response['response']['total_count']
        page_offset += num_comments_per_day
        total_comms_per_day.append(num_comments_per_day)
        day += 1
    return total_comms_per_day


def get_time_intervals_for_last_7_days():
    last_seven_days = []
    midnight_time = time(hour=0, minute=0)
    the_day = (datetime.now().date())

    day = 1
    while day != 8:
        day_before = (datetime.now() - timedelta(days=day)).date()
        dates = [
            (datetime.combine(the_day, midnight_time)).timestamp(),
            (datetime.combine(day_before, midnight_time)).timestamp()
        ]
        the_day = day_before
        last_seven_days.append(dates)
        day += 1
    return last_seven_days


def create_graphic(total_comments_everyday):
    days = [
        '1 day',
        '2 day',
        '3 day',
        '4 day',
        '5 day',
        '6 day',
        '7 day'
    ]
    fig = go.Figure([go.Bar(x=days, y=total_comments_everyday)])
    return fig


if __name__ == '__main__':
    everyday_comments_value = get_number_of_comments_by_day()
    create_graphic(everyday_comments_value).show()
