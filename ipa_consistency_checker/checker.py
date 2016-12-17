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
Module implements parallel state checking per multiple servers
"""

from __future__ import absolute_import

import logging
import time

from multiprocessing import Process, Queue
from six.moves import queue

from .registry import Registry

# Load all plugins, yes ugly but works
# pylint: disable=wildcard-import,unused-wildcard-import
from .plugins import *
# pylint: enable=wildcard-import,unused-wildcard-import

logger = logging.getLogger(__name__)
register = Registry()

class CheckerWorker(Process):
    """
    Subprocess, runs checks per one server
    """

    def __init__(self, parent_queue, server, password, plugins):
        super(CheckerWorker, self).__init__(name=server)
        self.queue = parent_queue
        self.server = server
        self.password = password
        self.plugins = plugins
        self.log = logging.getLogger(
            "{}.{}".format("worker", self.server))

    def run(self):
        return_state = {}

        for plugin_name, options in self.plugins:
            instance = Registry.get_plugin(plugin_name)(None, **options)
            result = instance.execute()
            return_state[plugin_name] = result

        self.queue.put((self.server, return_state))


class Checker(object):
    """
    Manages workers and collects states from all servers
    """
    @staticmethod
    def plugins():
        """Get list of available plugins (plugin names)
        :return: list of plugin names
        """
        return list(register)

    @staticmethod
    def plugins_help():
        """Generates help message in format
        plugin name - plugin description
        :return: help message
        """
        items = (
            "{:10} - {}".format(name, Registry.get_description(name))
            for name in sorted(register)
        )
        return '\n'.join(items)

    def __call__(self, servers, password, plugins, wait=120):
        q = Queue()
        results = {}
        workers = set()

        def get_data(queue_wait=2):
            """Collect data from queue added by workers
            :param queue_wait: time how long wait for new data (blocking)
            """
            empty = False
            while not empty:
                try:
                    server, data = q.get(True, queue_wait)
                except queue.Empty:
                    empty = True
                else:
                    results[server] = data

        logger.debug("Starting subprocesses ...")
        for server in servers:
            w = CheckerWorker(q, server, password, plugins)
            workers.add(w)
            w.start()

        logger.debug("Waiting ...")
        endtime = time.time() + wait
        is_alive = True
        while time.time() < endtime:
            get_data()

            if not is_alive:
                break

            is_alive = False
            for w in workers:
                is_alive = w.is_alive() or is_alive

        # make sure all data have been collected
        get_data()

        logger.debug("Cleanup ...")
        for w in workers:
            w.join(1)
            if w.is_alive():
                logger.error("terminating process %r", w)
                w.terminate()

        return results
