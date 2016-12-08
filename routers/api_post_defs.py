#!/usr/bin/env python
# -*- coding: utf-8 -*-,
import json


def test_handler(out_headers):
    """/api/test

    :param out_headers: header(content_type, status_code)
    """
    return json.dumps({
        'status': 'OK'
    })
