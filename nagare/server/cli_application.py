# --
# Copyright (c) 2008-2018 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import os

from nagare.admin import app_serve
from nagare.services import plugin
from nagare.server.services import Services


class CLIApp(plugin.Plugin):
    CONFIG_SPEC = {}

    def handle_start(self):
        pass

    @staticmethod
    def handle_request(chain, command, **arguments):
        return command.handle_request(**arguments)


class App(app_serve.Serve):
    def _create_service(self, config_filename, activated_by_default):
        return Services(
            config_filename, '', 'nagare.services', activated_by_default,
            app_name=self.name,
            here=os.path.dirname(config_filename) if config_filename else '',
            config_filename=config_filename or '',
            application={'name': 'cli'}, publisher={'type': 'cli'},
            **os.environ
        )

    def run(self, services_service, **arguments):
        return services_service(super(App, self).run, command=self, **arguments)
