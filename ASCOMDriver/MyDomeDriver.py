from ASCOMDriver.DeviceInterfaces.IDomeV2 import IDomeV2
from ASCOMDriver.DeviceInterfaces.Enumerations import ShutterState
from ASCOMDriver.MyDeviceDriver import MyDeviceDriver


class MyDomeDriver(MyDeviceDriver, IDomeV2):
    """This is an example of how a driver could be implemented
    Ref: https://github.com/ASCOMInitiative/ASCOMPlatform/blob/master/DriverTemplates/TemplateSources/src/ASCOM%20Driver%20Template%20(CS)/DeviceDome.cs
    """

    def __init__(self):
        super().__init__("MyASCOMDomeDriver", "My driver description")
        self.__interfaceversion = 0
        self.__canfindhome = True
        self.__canpark = True
        self.__cansetaltitude = False
        self.__cansetazimuth = False
        self.__cansetpark = False
        self.__cansetshutter = False
        self.__canslave = False
        self.__cansyncazimuth = False
        self.__description = "My Description"
        self.__driverinfo = "My Dome Description"
        self.__driverversion = "1.0"

        self.__shutterstatus = ShutterState.shutterClosed
        self.__slewing = False
        self.__athome = False
        self.__atpark = False
        self.__azimuth = 0
        pass

    #
    # IDomeV2
    #
    def InterfaceVersion(self):
        print("InterfaceVersion")
        return self.__interfaceversion

    def CanFindHome(self):
        print("CanFindHome")
        return self.__canfindhome

    def CanPark(self):
        print("CanPark")
        return self.__canpark

    def CanSetAltitude(self):
        print("CanSetAltitude")
        return self.__cansetaltitude

    def CanSetAzimuth(self):
        print("CanSetAzimuth")
        return self.__cansetazimuth

    def CanSetPark(self):
        print("CanSetPark")
        return self.__cansetpark

    def CanSetShutter(self):
        print("CanSetShutter")
        return self.__cansetshutter

    def CanSlave(self):
        print("CanSlave")
        return self.__canslave

    def CanSyncAzimuth(self):
        print("CanSyncAzimuth")
        return self.__cansyncazimuth

    def Description(self):
        print("Description")
        return self.__description

    def DriverInfo(self):
        print("DriverInfo")
        return self.__driverinfo

    def DriverVersion(self):
        print("DriverVersion")
        return self.__driverversion

    #------------------------------------------

    def CloseShutter(self):
        # Close shutter or otherwise shield telescope from the sky.
        self.__shutterstatus = ShutterState.shutterClosed  # TODO: Implement logic instead
        MyDeviceDriver.logger.info("Shutter is now closed")
        pass

    def OpenShutter(self):
        # Open shutter or otherwise expose telescope to the sky.

        self.__shutterstatus = ShutterState.shutterOpen  # TODO: Implement logic instead

        MyDeviceDriver.logger.info("Shutter is now open")
        pass

    def Park(self):
        # Open shutter or otherwise expose telescope to the sky.
        self.__shutterstatus = ShutterState.shutterOpen  # TODO: Implement logic instead
        MyDeviceDriver.logger.info("Dome is parking")
        pass

    @property
    def ShutterStatus(self, *args, **kwargs):
        # Indicates whether the dome is in the home position. Raises an error if not supported.
        print("ShutterStatus called")
        return self.__shutterstatus

    @property
    def Slewing(self, *args, **kwargs):
        print("Slewing called!")
        return self.__slewing

    @property
    def AtHome(self, *args, **kwargs):
        print("AtHome called!")
        return self.__athome

    @property
    def AtPark(self, *args, **kwargs):
        print("AtPark called!")
        return self.__atpark

    @property
    def Azimuth(self, *args, **kwargs):
        print("Azimuth called!")
        return self.__azimuth


if __name__ == "__main__":
    driver = MyDomeDriver()

    print("Initial status: %s" % driver.ShutterStatus)

    driver.OpenShutter()
    print(driver.ShutterStatus)

    driver.CloseShutter()
    print(driver.ShutterStatus)

    pass
