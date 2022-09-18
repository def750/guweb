# -*- coding: utf-8 -*-

from enum import IntFlag
from enum import unique

__all__ = ('Privileges',)

@unique
class Privileges(IntFlag):
    """Server side user privileges."""

    # privileges intended for all normal players.
    UNRESTRICTED  = 1 << 0 # is an unbanned player.
    VERIFIED      = 1 << 1 # has logged in to the server in-game.

    # has bypass to low-ceiling anticheat measures (trusted).
    WHITELISTED   = 1 << 2

    # donation tiers, receives some extra benefits.
    SUPPORTER     = 1 << 4
    PREMIUM       = 1 << 5

    # notable users, receives some extra benefits.
    ALUMNI        = 1 << 7

    # staff permissions, able to manage server state.
    TOURNAMENT    = 1 << 10 # able to manage match state without host.
    NOMINATOR     = 1 << 11 # able to manage maps ranked status.
    MODERATOR     = 1 << 12 # able to manage users (level 1).
    ADMINISTRATOR = 1 << 13 # able to manage users (level 2).
    DEVELOPER     = 1 << 14 # able to manage full server state.

    DONATOR = SUPPORTER | PREMIUM
    Staff = MODERATOR | ADMINISTRATOR | DEVELOPER
