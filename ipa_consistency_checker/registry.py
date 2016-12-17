# Authors:
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
Plugins register
"""

from __future__ import absolute_import

_registry = {}


class Registry(object):
    """A decorator for registering plugins

    Usage:

        register = Registry()

        @register()
        class plugin(...):
            ...

    """

    def __call__(self, name, description=None):
        def register(plugin):
            """
            Register the plugin ``plugin``.

            :param plugin: A subclass of `LDAPPlugin` to attempt to register.
            """

            # error if this exact class was already registered:
            if name in _registry:
                raise RuntimeError("Duplicated name {}:{!r}".format(
                    name, plugin))

            # The plugin is okay, add to _registry:
            _registry[name] = dict(plugin=plugin, description=description)

            return plugin

        return register

    def __iter__(self):
        return iter(_registry)

    @staticmethod
    def get_plugin(name):
        """Returns plugin reference
        :param name: plugin name
        :return: reference to plugin class
        """
        return _registry[name]['plugin']

    @staticmethod
    def get_description(name):
        """Returns plugin description
        :param name: plugin name
        :return: textual description
        """
        return _registry[name]['description']
