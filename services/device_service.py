#!/usr/bin/env python
#
# Copyright 2013 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete


class DeviceService(pyrestful.rest.RestHandler):

    def initConfig(self, config):
        self.__config = config

    @get(_path="/{device_type}/{device_number}/{resource}", _types=[str, int, str], _produces=mediatypes.APPLICATION_JSON)
    def getConnected(self, device_type, device_number, resource):
        if (self.__config.driver is None):
            raise ValueError("Driver is not present")
        else:
            # TODO use reflection to return the driver's property value (property name should be identical to resource name)
            raise NotImplementedError()

    # TODO PUT !