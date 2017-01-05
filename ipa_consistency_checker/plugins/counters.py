# Authors:
#   Peter Pakos <peter.pakos@wandisco.com>
#   Martin Basti <mbasti@redhat.com>
#
# Copyright (C) 2016  Peter Pakos <peter.pakos@wandisco.com>
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
Checker plugins which works as counters - count number of entries in LDAP
"""

from __future__ import absolute_import

import abc
import logging
import ldap
import six

from ipa_consistency_checker.plugins.absplugin import LDAPPlugin
from ipa_consistency_checker.registry import CheckerRegistry

logger = logging.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class Counter(LDAPPlugin):
    """
    Base class for counter plugins. Implements the logic.
    Subclasses must specifiy only 'container'

    Optional attributes:
      'ldapfilter': filter as string
    """
    ldapfilter = '(objectClass=*)'

    @abc.abstractproperty
    def container(self):
        """Container where entries are located
        for example: 'cn=users,cn=accounts'
        :return: container as string
        """
        return None

    def execute(self):
        result = self.conn.search_s(
            '{container},{suffix}'.format(
                container=self.container,
                suffix=self.options['suffix']),
            ldap.SCOPE_BASE,
            filterstr=self.ldapfilter,
            attrlist=['numSubordinates']
        )
        logger.debug("Result: %r", result)
        if len(result) != 1:
            logger.warning(
                "Unexpected number of results: %d, %s",
                len(result), self.container
            )
        return int(result[0][1]['numSubordinates'][0])


@CheckerRegistry.register('users', description='Active users')
class ActiveUsers(Counter):
    """
    Count number of active users
    """
    container = 'cn=users,cn=accounts'


@CheckerRegistry.register('ustage', description='Stage users')
class StageUsers(Counter):
    """
    Count number of stage users
    """
    container = 'cn=staged users,cn=accounts,cn=provisioning'


@CheckerRegistry.register('hosts', description='Hosts')
class Hosts(Counter):
    """
    Count number of hosts
    """
    container = 'cn=computers,cn=accounts'
