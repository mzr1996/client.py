import inspect

import deebot_client.events
from deebot_client.events import Event
from deebot_client.events.const import EVENT_DTO_REFRESH_COMMANDS


def test_events_has_refresh_function():
    for name, obj in inspect.getmembers(deebot_client.events, inspect.isclass):
        if issubclass(obj, Event) and obj != Event:
            assert obj in EVENT_DTO_REFRESH_COMMANDS