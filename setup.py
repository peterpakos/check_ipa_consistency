#!/usr/bin/python

# Authors:
#   Martin Basti <mbasti@redhat.com>
#
# Copyright (C) 2017  Peter Pakos <peter.pakos@wandisco.com>
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

from setuptools import setup, find_packages

setup(
    name="ipa-check-consistency",
    version="17.1.17",
    packages=find_packages(),

    scripts=['ipa-check-consistency'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'pyldap',
        'pyaml',
        'six',
        'tabulate',
    ],

    # metadata for upload to PyPI
    author="Peter Pakos",
    author_email="peter.pakos@wandisco.com",
    description="Checks consistency across FreeIPA servers",
    license="GPL3+",
    keywords="freeipa check consistency ldap",
    url="https://github.com/peterpakos/ipa_check_consistency",
)
