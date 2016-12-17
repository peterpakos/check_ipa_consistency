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

from ipa_consistency_checker.plugins.absplugin import LDAPPlugin
from ipa_consistency_checker.registry import CheckerRegistry


@CheckerRegistry.register('users', description='Active users')
class UsersCount(LDAPPlugin):
    """
    Count number of active users
    """
    def execute(self):
        return 'Ahoj'
