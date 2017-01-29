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
Tests for counter based plugins
"""
from __future__ import absolute_import
import ldap

from ipa_consistency_checker.tests.util import MockLDAP
from ipa_consistency_checker.plugins.counters import (
    ActiveUsers,
    StageUsers,
    PreservedUsers,
    UserGroups,
    Hosts,
    HostGroups,
    HBACRules,
    SUDORules,
    DNSZones,
)

suffix = 'o=test'
filter_all = '(objectClass=*)'

num_active_users = 10
dn_active_users = 'cn=users,cn=accounts,{}'.format(suffix)

num_stage_users = 20
dn_stage_users = 'cn=staged users,cn=accounts,cn=provisioning,{}'.format(suffix)

num_preserved_users = 30
dn_preserved_users = 'cn=deleted users,cn=accounts,cn=provisioning,{}'.format(suffix)

num_hosts = 40
dn_hosts = 'cn=computers,cn=accounts,{}'.format(suffix)

num_host_groups = 50
dn_host_groups = 'cn=hostgroups,cn=accounts,{}'.format(suffix)

dn_user_groups = 'cn=groups,cn=accounts,{}'.format(suffix)
result_user_groups = [
    ('cn={}'.format(gr) + dn_user_groups, {'cn': gr})
    for gr in ('gr1', 'gr2', 'gr3')
]

dn_hbac = 'cn=hbac,{}'.format(suffix)
result_hbac = [
    ('ipaUniqueID={}'.format(iuid) + dn_hbac, {'ipaUniqueID': iuid})
    for iuid in ('0001', '0002', '0003', '0004')
]

dn_sudo_rules = 'cn=sudorules,cn=sudo,{}'.format(suffix)
result_sudo_rules = [
    ('ipaUniqueID={}'.format(iuid) + dn_sudo_rules, {'ipaUniqueID': iuid})
    for iuid in ('1001', '1002', '1003', '1004', '1005')
]

dn_dns_zones = 'cn=dns,{}'.format(suffix)
result_dns_zones = [
    ('idnsname={}'.format(zone) + dn_dns_zones, {'idnsname': zone})
    for zone in ('zone1', 'zone2', 'zone3')
]


search_mapping = {
    (
        dn_active_users,
        ldap.SCOPE_BASE,  # pylint: disable=no-member
        filter_all
    ): [(
        dn_active_users, {
            'numSubordinates': [str(num_active_users)]
        },
    )],
    (
        dn_stage_users,
        ldap.SCOPE_BASE,  # pylint: disable=no-member
        filter_all
    ): [
        (dn_stage_users, {
            'numSubordinates': [str(num_stage_users)]
        },
        )],
    (
        dn_preserved_users,
        ldap.SCOPE_BASE,  # pylint: disable=no-member
        filter_all
    ): [
        (dn_preserved_users, {
            'numSubordinates': [str(num_preserved_users)]
        },
        )],
    (
        dn_hosts,
        ldap.SCOPE_BASE,  # pylint: disable=no-member
        filter_all
    ): [
        (dn_hosts, {
            'numSubordinates': [str(num_hosts)]
        },
        )],
    (
        dn_host_groups,
        ldap.SCOPE_BASE,  # pylint: disable=no-member
        filter_all
    ): [
        (dn_host_groups, {
            'numSubordinates': [str(num_host_groups)]
        },
        )],
    (
        dn_user_groups,
        ldap.SCOPE_ONELEVEL,  # pylint: disable=no-member
        '(objectClass=ipausergroup)'
    ):
        result_user_groups,
    (
        dn_hbac,
        ldap.SCOPE_ONELEVEL,  # pylint: disable=no-member
        '(ipaUniqueID=*)'
    ):
        result_hbac,
    (
        dn_sudo_rules,
        ldap.SCOPE_ONELEVEL,  # pylint: disable=no-member
        '(ipaUniqueID=*)'
    ):
        result_sudo_rules,
    (
        dn_dns_zones,
        ldap.SCOPE_ONELEVEL,  # pylint: disable=no-member
        '(|(objectClass=idnszone)(objectClass=idnsforwardzone))'
    ):
        result_dns_zones,
}

ldap_conn = MockLDAP(search_mapping)


def test_active_users():
    """
    Test Active Users counter
    """
    plugin = ActiveUsers(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == num_active_users


def test_stage_users():
    """
    Test Stage Users counter
    """
    plugin = StageUsers(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == num_stage_users


def test_preserved_users():
    """
    Test Preserved Users counter
    """
    plugin = PreservedUsers(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == num_preserved_users


def test_hosts():
    """
    Test Hosts counter
    """
    plugin = Hosts(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == num_hosts


def test_host_groups():
    """
    Test Host Groups counter
    """
    plugin = HostGroups(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == num_host_groups


def test_user_groups():
    """
    Test User Groups counter
    """
    plugin = UserGroups(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == len(result_user_groups)


def test_hbac_rules():
    """
    Test HBAC rules counter
    """
    plugin = HBACRules(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == len(result_hbac)


def test_sudo_rules():
    """
    Test sudo rules counter
    """
    plugin = SUDORules(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == len(result_sudo_rules)


def test_dns_zones():
    """
    Test dns zones counter
    """
    plugin = DNSZones(ldap_conn, suffix=suffix)
    result = plugin.execute()
    assert result == len(result_dns_zones)
