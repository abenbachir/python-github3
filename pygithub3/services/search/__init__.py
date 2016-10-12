#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service
from .search_users import SearchUsers


class Search(Service):
    """ Consume `Users API <http://developer.github.com/v3/search>`_ """

    def __init__(self, **config):
        super(Search, self).__init__(**config)
        self.search_users = SearchUsers(**config)


