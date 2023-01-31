# Encoding: utf-8

# --
# Copyright (c) 2008-2023 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare import commands
from nagare.services import base_exceptions_handler


def default_handler(exception, exceptions_service, **context):
    if isinstance(exception, KeyboardInterrupt):
        status = 130
    elif isinstance(exception, commands.CommandError):
        if exception.message:
            print('error: {}'.format(exception.message))

        status = exception.status
    else:
        exceptions_service.log_exception()
        status = 1

    return status


class Exceptions(base_exceptions_handler.ExceptionsService):
    LOAD_PRIORITY = base_exceptions_handler.ExceptionsService.LOAD_PRIORITY + 1

    CONFIG_SPEC = dict(
        base_exceptions_handler.ExceptionsService.CONFIG_SPEC,
        exception_handler='string(default="nagare.services.cli_exceptions_handler:default_handler")',
    )
