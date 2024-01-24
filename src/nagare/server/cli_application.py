# --
# Copyright (c) 2008-2024 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import sys

from nagare.admin import app_serve
from nagare.config import config_from_dict
from nagare.services import plugin


class CLIApp(plugin.Plugin):
    def handle_start(self, app):
        pass

    def handle_request(self, chain, command, **arguments):
        config = self.plugin_config.copy()
        del config['activated']

        return command.handle_request(arguments=arguments, **config)


class App(app_serve.Serve):
    def __init__(self):
        super(App, self).__init__()
        sys.exit(self.execute())

    def handle_start(self, app):
        pass

    def _create_services(self, config, config_filename):
        mandatory_config = {
            'application': {'name': 'cli'},
            'publisher': {'type': 'cli'},
            'reloader': {'activated': 'off'},
        }
        config.merge(config_from_dict(mandatory_config))

        return super(App, self)._create_services(config, config_filename)

    def run(self, services_service, **arguments):
        return services_service(super(App, self).run, command=self, **arguments)
