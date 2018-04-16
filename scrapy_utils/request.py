import json

from scrapy.http import Request


class JsonRequest(Request):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            'headers',
            {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
        )
        kwargs.setdefault('method', 'POST')

        if 'json_body' in kwargs:
            kwargs.setdefault('body', json.dumps(kwargs['json_body']))
            del kwargs['json_body']

        super().__init__(*args, **kwargs)
