#!/usr/bin/env python
# -*- coding: utf-8 -*-,

from configuration.loadcfg import CFG
import MySQLdb


class Database(object):
    """docstring for Database"""
    _db = None

    @classmethod
    def init(cls):
        try:
            Database._db = MySQLdb.connect(**CFG['mysql'])
        except Exception as e:
            print e

    @classmethod
    def get(cls):
        return cls._db

    @classmethod
    def cursor(cls):
        return cls._db.cursor() if cls._db is not None else None
