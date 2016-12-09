#!/usr/bin/env python
# -*- coding: utf-8 -*-,
import json
from db.Database import Database as db


def test_handler(out_headers, post_data):
    """/api/test

    :param out_headers: header(content_type, status_code)
    :param post_data: the data passed via POST
    """
    print json.dumps(post_data)
    data_dict = dict()
    try:
        data_dict = json.loads(post_data)
        data_dict['status'] = 'OK'
    except (ValueError, ):
        data_dict['status'] = 'ERROR'
    return json.dumps(data_dict)


def new_action(out_headers, post_data):
    """/api/addaction

    :param out_headers: header(content_type, status_code)
    :param post_data: the data passed via POST
    """
    data_dict = dict()
    status = None
    try:
        data_dict = json.loads(post_data)
        status = 'OK'
    except (ValueError, ):
        status = 'ERROR'

    ret = dict(status=status)
    if status != 'OK':
        out_headers['status_code'] = 404
        return json.dumps(ret)

    db.init()
    connection = db.get()
    cursor = db.cursor()
    sql_statement = """
        INSERT INTO Bid(ts, id_Status, id_Action)
        VALUES (FROM_UNIXTIME(%s), %s, %s)
    """.strip()
    try:
        cursor.execute(sql_statement, (
            data_dict['ts'],
            data_dict['statusId'],
            data_dict['actionId']
        ))
        connection.commit()
    except:
        connection.rollback()
        ret['status'] = 'ERROR'
        out_headers['status_code'] = 500
        return json.dumps(ret)

    sql_statement = """
        SELECT id FROM Bid
        ORDER BY id DESC
        LIMIT 1
    """.strip()
    cursor.execute(sql_statement)
    id_bid = cursor.fetchone()[0]

    sql_statement = """
        INSERT INTO BiddingMap(id_Bidder, id_Bid)
        VALUES(%s, %s)
    """.strip()
    try:
        cursor.execute(sql_statement, (
            data_dict['bidderId'],
            id_bid
        ))
        connection.commit()
    except:
        connection.rollback()
        ret['status'] = 'ERROR'
        out_headers['status_code'] = 500
        return json.dumps(ret)
    connection.close()

    return json.dumps(ret)
