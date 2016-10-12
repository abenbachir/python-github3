# -*- encoding: utf-8 -*-

import requests
from pprint import pprint
from mock import patch

from pygithub3.core.client import Client
from pygithub3.exceptions import ValidationError
from pygithub3.services.search.search_users import SearchUsers
from pygithub3.tests.utils.base import (dummy_json, mock_response,
    mock_response_result)
from pygithub3.tests.utils.core import TestCase
from pygithub3.tests.utils.services import _


@dummy_json
@patch.object(requests.sessions.Session, 'request')
class TestSearchUsersService(TestCase):

    def setUp(self):
        self.search_users = SearchUsers()

    # def test_GET_without_user(self, request_method):
    #     request_method.return_value = mock_response()
    #     self.us.get()
    #     self.assertEqual(request_method.call_args[0], ('get', _('user')))

    def test_GET_LIST(self, request_method):
        request_method.return_value = mock_response()
        result = self.search_users.list(query='abder')
        # self.assertEqual(request_method.call_args[0],  ('get', _('users/octocat')))


