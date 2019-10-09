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

import os

import rqdatac

from rqalpha.utils.logger import system_log
from rqalpha.interface import AbstractMod


class RQDataMod(AbstractMod):
    def start_up(self, env, mod_config):
        if os.environ.get("RQDATAC2_CONF") or os.environ.get("RQDATAC_CONF"):
            system_log.info('rqdatac use RQDATAC2_CONF or RQDATAC_CONF')
            rqdatac.init()
        else:
            addr = (mod_config.rqdata_client_addr, mod_config.rqdata_client_port)
            env.system_log.info('rqdatac use address {}', addr)
            rqdatac.init(
                username=mod_config.rqdata_client_username,
                password=mod_config.rqdata_client_password,
                addr=addr,
                lazy=True
            )

        # noinspection PyUnresolvedReferences
        from rqdatac import fundamentals, Fundamentals, financials, Financials, fenji, query
        from rqalpha.api.api_base import register_api

        register_api("fundamentals", fundamentals)
        register_api("Fundamentals", Fundamentals)
        register_api("financials", financials)
        register_api("Financials", Financials)
        register_api("fenji", fenji)
        register_api("query", query)

    def tear_down(self, code, exception=None):
        pass

