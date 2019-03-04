import os
from datetime import datetime
import webbrowser

import meetup.api
from meetup.exceptions import ApiKeyError


def get_group_next_event(urlname='slcpython', key=''):
    # TODO: convert to async def
    client = meetup.api.Client(key)
    group_info = client.GetGroup({'urlname': urlname})
    return group_info.next_event


def howdy(key=''):
    try:
        api_key = os.environ.get('MEETUP_API_KEY', key)
        next_event_info = get_group_next_event(key=api_key)
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
    except (ApiKeyError, KeyError):
        msg = """
        Sorry, we couldn't find a MEETUP_API_KEY.
        Please set one up by visiting
        https://secure.meetup.com/meetup_api/key/
        Then, `export MEETUP_API_KEY=<key>` before
        running this command.
        Alternatively, you may add a `key` argument
        to `howdy`. Eg, `slcpython.howdy(key='<KEY>')`
        """

    print(msg)
