# Authors:
#   Martin Basti <mbasti@redhat.com>
#
# Copyright (C) 2017  Martin Basti <mbasti@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Utils for tests
"""
from __future__ import absolute_import
import ldap


class MockLDAP(object):
    """
    Very basic mock LDAP
    """

    def __init__(self, search_mapping):
        """
        Creates an LDAP connection object, support only search operation and
        NO_SUCH_OBJECT exception
        :param search_mapping: {(base, scope, filter): result, ...}
        """
        self.search_mapping = search_mapping

    def search_s(
            self, base, scope, filterstr='(objectClass=*)',
            attrlist=None, attrsonly=0):  # pylint: disable=unused-argument
        """
        Mocked search operation, parameters are the same as ldap module has
        :param base: base DN
        :param scope: search scope
        :param filterstr: requires to have specified filter mappings
        :param attrlist: not implemented
        :param attrsonly: not implemented
        :return: result that matches (base, scope, filterstr) in search_mapping
        """
        result = self.search_mapping.get((base, scope, filterstr))
        if result is None:
            raise ldap.NO_SUCH_OBJECT  # pylint: disable=no-member
        else:
            return result
