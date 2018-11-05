# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.

import pkgutil

BLUEP_PRINTS_TYPE = ['BLUE_PRINT', 'BLUE_PRINT_PUBLIC']
BLUEPRINTS = []
__all__ = []

# dynamical load sub blueprints
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    for bpt in BLUEP_PRINTS_TYPE:
        try:
            bp = getattr(module, bpt)
            if bp:
                BLUEPRINTS.append((bp, bpt))
        except AttributeError:
            pass
