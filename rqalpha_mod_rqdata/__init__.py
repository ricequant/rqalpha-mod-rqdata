# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


from rqalpha import cli

from .mod import RQDataMod


def load_mod():
    return RQDataMod()


__config__ = {
    "rqdata_client_addr": "rqdatad.ricequant.com",
    "rqdata_client_port": 16003,
    "rqdata_client_username": "username",
    "rqdata_client_password": "password",
}

cli_prefix = "mod__ricequant_data__"

cli.commands['run'].params.append(
    click.Option(
        ('-rdu', '--rqdatad-username', cli_prefix + 'rqdata_client_username'),
        type=click.STRING,
        help="[ricequant_data] rqdatad username",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('-rdpw', '--rqdatad-password', cli_prefix + 'rqdata_client_password'),
        type=click.STRING,
        help="[ricequant_data] rqdatad password",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('-rda', '--rqdatad-addr', cli_prefix + 'rqdata_client_addr'),
        type=click.STRING,
        help="[ricequant_data] rqdatad server address",
    )
)
cli.commands['run'].params.append(
    click.Option(
        ('-rdpt', '--rqdatad-port', cli_prefix + 'rqdata_client_port'),
        type=click.INT,
        help="[ricequant_data] rqdatad server port",
    )
)
