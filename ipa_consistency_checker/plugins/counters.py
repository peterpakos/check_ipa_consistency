"""
Checker plugins which works as counters - count number of entries in LDAP
"""

from __future__ import absolute_import

from ipa_consistency_checker.plugins.absplugin import LDAPPlugin, Registry

register = Registry()


@register('users', description='Active users')
class UsersCount(LDAPPlugin):
    """
    Count number of active users
    """
    def execute(self):
        return 'Ahoj'
