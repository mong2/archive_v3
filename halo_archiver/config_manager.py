"""Configuration helper class.  Holds all config things."""


class ConfigManager(object):
    """This class is used to manage all configuration information for the
    keyhelper module.  It will attempt to determine info from environment
    variables.

    """
    def __init__(self, halo_key, halo_secret):
        self.halo_key = halo_key
        self.halo_secret = halo_secret
