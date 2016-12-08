#!/usr/bin/env python
# -*- coding: utf-8 -*-,
import json
from db.Database import Database as db


def test_handler(out_headers):
    """/api/test

    :param out_headers: header(content_type, status_code)
    """
    ret = {
        'status': 'OK' if out_headers['status_code'] != 404 else 'ERROR',
        'data': []
    }
    return json.dumps(ret)


def statuses(out_headers):
    """/api/statuses

    :param out_headers: header(content_type, status_code)
    """
    db.init()
    cursor = db.cursor()
    cursor.execute('SELECT id, value FROM Status')
    response_body = json.dumps({
        'status': 'OK',
        'data': map(lambda x: {
            'id':     x[0],
            'value':  x[1]
        }, cursor.fetchall())
    })
    db.get().close()

    return response_body


def bidders(out_headers):
    """/api/bidders

    :param out_headers: header(content_type, status_code)
    """
    db.init()
    cursor = db.cursor()
    cursor.execute('SELECT id, firstname, lastname FROM Bidder')
    response_body = json.dumps({
        'status': 'OK',
        'data': map(lambda x: {
            'id':        x[0],
            'FullName':  '%s %s' % (x[1], x[2])
        }, cursor.fetchall())
    })
    db.get().close()

    return response_body


def actions(out_headers):
    """/api/actions

    :param out_headers: header(content_type, status_code)
    """
    db.init()
    cursor = db.cursor()
    cursor.execute('SELECT id, value FROM Action')
    response_body = json.dumps({
        'status': 'OK',
        'data': map(lambda x: {
            'id':     x[0],
            'value':  x[1]
        }, cursor.fetchall())
    })
    db.get().close()

    return response_body


def init(out_headers):
    """/api/init

    :param out_headers: header(content_type, status_code)
    """
    db.init()
    cursor = db.cursor()
    sql_statement = """
        SELECT  BM.id,
                firstname,
                lastname,
                UNIX_TIMESTAMP(ts),
                Status.value AS status_value,
                Action.value AS action_value
        FROM
                (
                    (
                        (
                            BiddingMap BM LEFT JOIN Bidder ON BM.id_Bidder = Bidder.id
                        ) LEFT JOIN Bid ON BM.id_Bid = Bid.id
                    ) LEFT JOIN Status ON Bid.id_Status = Status.id
                ) LEFT JOIN Action ON Bid.id_Action = Action.id;
    """.strip()
    cursor.execute(sql_statement)
    response_body = json.dumps({
        'status': 'OK',
        'data': map(lambda x: {
            'Id':         x[0],
            'FirstName':  x[1],
            'LastName':   x[2],
            'Date':       x[3],
            'Status':     x[4],
            'Action':     x[5]
        }, cursor.fetchall())
    })
    db.get().close()

    return response_body
