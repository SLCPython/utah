import os
from datetime import datetime

import meetup.api
from meetup.exceptions import ApiKeyError


def get_group_next_event(urlname='slcpython'):
    # TODO: convert to async def
    api_key = os.environ['MEETUP_API_KEY']
    client = meetup.api.Client()
    group_info = client.GetGroup({'urlname': urlname})
    return group_info.next_event


def howdy():
    try:
        next_event_info = get_group_next_event()
        next_datetime = datetime.fromtimestamp(
                next_event_info['time'] / 1000.0)
        datefmt = r'%A, %B %-d'
        timefmt = r'%-I:%M%p'
        time_msg = f"{next_datetime.strftime(datefmt)}, at {next_datetime.strftime(timefmt).lower()}"

        msg = f"""
            Howdy, Salt Lake City! 🤠
            "Our next meetup is on:"
            "{time_msg}"
            "and is about:"
            "{next_event_info['name']}"
            """
    except ApiKeyError:
        print('Meetup API key not set')

    print(msg)
