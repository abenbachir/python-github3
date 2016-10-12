#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from . import Request
from pygithub3.resources.search import SearchUsers


class List(Request):

    resource = SearchUsers
    uri = 'search/users'

