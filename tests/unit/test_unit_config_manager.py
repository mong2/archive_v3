"""Unit tests for config_manager.py"""

import imp
import os
import pytest
import sys

module_name = 'halo_archiver'

here_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(here_dir, '../../')
sys.path.append(module_path)
fp, pathname, description = imp.find_module(module_name)

halo_archiver = imp.load_module(module_name, fp, pathname, description)


class TestConfigManager:
    def test_config_manager_create(self):
        confman = halo_archiver.ConfigManager("HALOKEY", "HALOSECRET")
        return confman
