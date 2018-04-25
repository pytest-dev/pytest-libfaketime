# -*- coding: utf-8 -*-

import os
import libfaketime


def pytest_configure(config):
    needs_reload, env_additions = libfaketime.get_reload_information()
    if needs_reload:
        capture_manager = config.pluginmanager.getplugin('capturemanager')
        capture_manager.stop_global_capturing()
        libfaketime.reexec_if_needed()
        os.environ.update(env_additions)
