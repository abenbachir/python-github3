#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pygithub3.services.base import Service
from pprint import pprint

class SearchUsers(Service):
    """ Consume `Followers API
    <https://developer.github.com/v3/search/#search-users>`_
    """

    def list(self, query=None, sort=None, order=None):

        request = self.request_builder('search.search_users.list', query=query, sort=sort, order=order)

        return self._get(request, q=query)




