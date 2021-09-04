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

from .device_service import DeviceService


class DomeService(DeviceService):

    # SHOULD BE IMPLEMENTED HERE ONLY THE RESOURCES WHICH CANNOT BE EASILY QUERIED ONTO
    # THE ASCOM DRIVER USING REFLECTION AT THE DeviceService LEVEL.

    @get(_path="/api/v1/{device_type}/{device_number}/interfaceversion", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getInterfaceVersion(self, device_type, device_number):
        super().getResource(device_type, device_number, "InterfaceVersion")

    @get(_path="/api/v1/{device_type}/{device_number}/canfindhome", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanFindHome(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanFindHome")

    @get(_path="/api/v1/{device_type}/{device_number}/canpark", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanPark(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanPark")

    @get(_path="/api/v1/{device_type}/{device_number}/cansetaltitude", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanSetAltitude(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanSetAltitude")

    @get(_path="/api/v1/{device_type}/{device_number}/cansetazimuth", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanSetAzimuth(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanSetAzimuth")

    @get(_path="/api/v1/{device_type}/{device_number}/cansetpark", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanSetPark(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanSetPark")

    @get(_path="/api/v1/{device_type}/{device_number}/cansetshutter", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanSetShutter(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanSetShutter")

    @get(_path="/api/v1/{device_type}/{device_number}/canslave", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanSlave(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanSlave")

    @get(_path="/api/v1/{device_type}/{device_number}/cansyncazimuth", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getCanSyncAzimuth(self, device_type, device_number):
        super().getResource(device_type, device_number, "CanSyncAzimuth")

    @get(_path="/api/v1/{device_type}/{device_number}/description", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getDescription(self, device_type, device_number):
        super().getResource(device_type, device_number, "Description")

    @get(_path="/api/v1/{device_type}/{device_number}/driverinfo", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getDriverInfo(self, device_type, device_number):
        super().getResource(device_type, device_number, "DriverInfo")

    @get(_path="/api/v1/{device_type}/{device_number}/driverversion", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def getDriverVersion(self, device_type, device_number):
        super().getResource(device_type, device_number, "DriverVersion")

    # -----------------------------------------------------
    @get(_path="/api/v1/{device_type}/{device_number}/shutterstatus", _types=[str, str], _produces=mediatypes.APPLICATION_JSON)
    def getShutterState(self, device_type, device_number):
        super().getResource(device_type, device_number, "ShutterStatus")

    # ---------------------------------------------------

    @put(_path="/api/v1/{device_type}/{device_number}/openshutter", _types=[str, str], _produces=mediatypes.APPLICATION_JSON)
    def openShutter(self, device_type, device_number):
        super().getResource(device_type, device_number, "OpenShutter")

    @put(_path="/api/v1/{device_type}/{device_number}/closeshutter", _types=[str, str], _produces=mediatypes.APPLICATION_JSON)
    def closeShutter(self, device_type, device_number):
        super().getResource(device_type, device_number, "CloseShutter")

    @put(_path="/api/v1/{device_type}/{device_number}/park", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def putPark(self, device_type, device_number):
        super().getResource(device_type, device_number, "Park")

    #---------------------------------------------

    @get(_path="/api/v1/{device_type}/{device_number}/slewing", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def slewing(self, device_type, device_number):
        super().getResource(device_type, device_number, "Slewing")

    @get(_path="/api/v1/{device_type}/{device_number}/athome", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def athome(self, device_type, device_number):
        super().getResource(device_type, device_number, "AtHome")

    @get(_path="/api/v1/{device_type}/{device_number}/atpark", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def atpark(self, device_type, device_number):
        super().getResource(device_type, device_number, "AtPark")

    @get(_path="/api/v1/{device_type}/{device_number}/azimuth", _types=[str, str],
         _produces=mediatypes.APPLICATION_JSON)
    def azimuth(self, device_type, device_number):
        super().getResource(device_type, device_number, "Azimuth")