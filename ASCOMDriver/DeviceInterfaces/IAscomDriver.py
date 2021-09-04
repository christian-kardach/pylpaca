import abc


class IAscomDriver(abc.ABC):
    """ASCOM.Interface ASCOM Driver Common Base Interface"""

    @abc.abstractproperty
    def Connected(self):
        # Set True to enable the link. Set False to disable the link.
        pass

    @property
    def Description(self):
        # Returns a description of the driver
        pass

    @property
    def Name(self):
        # Returns a description of the driver
        pass
