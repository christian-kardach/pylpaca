import abc
from .IAscomDriver import IAscomDriver
from .IDeviceControl import IDeviceControl
from .Enumerations import ShutterState


class IDomeV2(IAscomDriver, IDeviceControl):
    """This interface is used to handle a dome, with or without a controllable shutter, and also a roll off roof.
    Ref: https://github.com/ASCOMInitiative/ASCOMPlatform/blob/master/ASCOM.DeviceInterface/IDomeV2.vb
    """
    # TODO: Finish all declarations

    @property
    def CloseShutter(self):
        # Close shutter or otherwise shield telescope from the sky.
        print("CloseShutter")
        pass

    @property
    def OpenShutter(self):
        # Open shutter or otherwise expose telescope to the sky.
        print("OpenShutter")
        pass

    @property
    def ShutterStatus(self):
        # Indicates whether the dome is in the home position. Raises an error if not supported.
        print("ShutterStatus")
        pass

    @property
    def AtHome(self):
        # Indicates whether the dome is in the home position. Raises an error if not supported.
        print("AtHome")
        pass
