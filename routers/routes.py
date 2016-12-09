#!/usr/bin/env python
# -*- coding: utf-8 -*-,
import json
import api_get_defs
import api_post_defs

ROOTS = ('/', '/index', '/index.html', )
ROUTER = {
    'GET': {
        '/api/test':      api_get_defs.test_handler,
        '/api/statuses':  api_get_defs.statuses,
        '/api/bidders':   api_get_defs.bidders,
        '/api/actions':   api_get_defs.actions,
        '/api/init':      api_get_defs.init,
    },

    'POST': {
        '/api/test':       api_post_defs.test_handler,
        '/api/newaction':  api_post_defs.new_action
    }
}


def api_get(out_headers, path):
    """api route for GET requests

    :param out_headers: dict(status_code, content_type)
    :param path: str; point access as an url
    """
    matched = filter(lambda key: path.startswith(key),
                     ROUTER['GET'].iterkeys())
    if matched:
        route_key = matched[0]
        try:
            return ROUTER['GET'][route_key](out_headers)
        except KeyError:
            pass

    out_headers['status_code'] = 404
    return json.dumps({
        'status': 'ERROR'
    })


def api_post(out_headers, path, data):
    """api route for POST requests

    :param out_headers: dict(status_code, content_type)
    :param path: str; point access as an url
    :param data: str; the data passed via POST
    """
    matched = filter(lambda key: path.startswith(key),
                     ROUTER['POST'].iterkeys())
    if matched:
        route_key = matched[0]
        try:
            return ROUTER['POST'][route_key](out_headers, data)
        except KeyError:
            pass

    out_headers['status_code'] = 404
    return json.dumps({
        'status': 'ERROR'
    })
