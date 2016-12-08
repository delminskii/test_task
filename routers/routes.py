#!/usr/bin/env python
# -*- coding: utf-8 -*-,
import json
import re
import api_get_defs
import api_post_defs

ROOTS = ('/', '/index', '/index.html', )
ROUTER = {
    'GET': {
        '/api/test':      api_get_defs.test_handler,
        '/api/statuses$':  api_get_defs.statuses,
        '/api/bidders$':   api_get_defs.bidders,
        '/api/actions$':   api_get_defs.actions,
        '/api/init$':      api_get_defs.init,
    },

    'POST': {

    }
}


def api_get(out_headers, path):
    """api route for GET requests

    :param out_headers: dict(status_code, content_type)
    """
    try:
        if not any(re.match(key, path, re.I | re.M | re.U) for key in ROUTER['GET'].iterkeys()):
            raise ValueError
        return ROUTER['GET'][path](out_headers)
    except (KeyError, ValueError):
        pass

    out_headers['status_code'] = 404
    return json.dumps({
        'status': 'ERROR'
    })


def api_post(out_headers, path):
    """api route for POST requests

    :param out_headers: dict(status_code, content_type)
    """
    # TODO
    pass
