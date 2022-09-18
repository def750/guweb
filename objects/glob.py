# -*- coding: utf-8 -*-

__all__ = ('db', 'http', 'version', 'cache')

from typing import TYPE_CHECKING

import settings  # imported for indirect use

if TYPE_CHECKING:
    from aiohttp import ClientSession
    import databases
    from cmyui.version import Version

db: 'databases.Database'
http: 'ClientSession'
version: 'Version'

cache = {
    'bcrypt': {}
}
