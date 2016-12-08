#!/usr/bin/env python
# -*- coding: utf-8 -*-,
import json
from db.Database import Database as db


def test_handler(out_headers, post_data):
    """/api/test

    :param out_headers: header(content_type, status_code)
    :param path: str; point acess as an url
    :param post_data: the data passed via POST
    """
    print 'TYPE: ', type(post_data)
    print 'DATA: ', post_data

    return json.dumps({
        'status': 'OK'
    })
