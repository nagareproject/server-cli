# --
# Copyright (c) 2008-2019 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import sys

from nagare.admin import app_serve
from nagare.services import plugin


class CLIApp(plugin.Plugin):

    def handle_start(self, app):
        pass

    @staticmethod
    def handle_request(chain, command, **arguments):
        return command.handle_request(**arguments)


class App(app_serve.Serve):

    def __init__(self):
        super(App, self).__init__()
        sys.exit(self.execute())

    def handle_start(self, app):
        pass

    def _create_services(self, config, config_filename, **vars):
        return super(App, self)._create_services(
            config, config_filename,
            app_name=self.name,
            application={'name': 'cli'},
            **vars
        )

    def run(self, services_service, **arguments):
        return services_service(super(App, self).run, command=self, **arguments)
