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
import abc
import six

_registry_checker = {}


@six.add_metaclass(abc.ABCMeta)
class Registry(object):
    """A decorator for registering plugins

    Usage:

        @Registry.register(test, description="Test Plugin")
        class plugin(...):
            ...

    """
    @classmethod
    @abc.abstractproperty
    def _storage(cls):
        return None

    @classmethod
    def register(cls, name, description=None):
        """
        Will register checker plugin
        :param name: name of checker plugin
        :param description: description of checker plugin
        :return:
        """
        def register(plugin):
            """
            Register the plugin ``plugin``.

            :param plugin: A subclass of `LDAPPlugin` to attempt to register.
            """

            # error if this exact class was already registered:
            if name in _registry_checker:
                raise RuntimeError("Duplicated name {}:{!r}".format(
                    name, plugin))

            # The plugin is okay, add to _registry:
            cls._storage[name] = dict(
                plugin=plugin, description=description)

            return plugin

        return register

    @classmethod
    def iter_names(cls):
        """Return iterator for checker plugins
        :return: interator
        """
        return iter(cls._storage)

    @classmethod
    def get_plugin(cls, name):
        """Returns plugin reference
        :param name: plugin name
        :return: reference to plugin class
        """
        return cls._storage[name]['plugin']

    @classmethod
    def get_description(cls, name):
        """Returns plugin description
        :param name: plugin name
        :return: textual description
        """
        return cls._storage[name]['description']


class CheckerRegistry(Registry):
    """
    Register for checker plugins
    """
    _storage = _registry_checker
