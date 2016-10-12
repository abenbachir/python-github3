#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Resource
from .users import User

__all__ = ('SearchUsers', 'SearchIssues')


class SearchUsers(Resource):
    _maps = {'user': User}
    def __str__(self):
        return '<SearchUsers (%s)>' % getattr(self, 'login', '')


class SearchIssues(Resource):

    def __str__(self):
        return '<SearchIssues (%s)>' % getattr(self, 'title', '')


