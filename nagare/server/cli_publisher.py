# --
# Copyright (c) 2008-2018 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare.server import publisher


class Publisher(publisher.Publisher):
    INTERNAL_RELOADER = True

    def _serve(self, app, **params):
        return self.start_handle_request(app, **params)
