# --
# Copyright (c) 2008-2024 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.server import publisher


class Publisher(publisher.Publisher):
    def _serve(self, app, activated, services_service, **params):
        return self.start_handle_request(app, services_service, **params)
