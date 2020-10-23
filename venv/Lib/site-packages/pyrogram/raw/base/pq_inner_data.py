#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PQInnerData = Union[raw.types.PQInnerData, raw.types.PQInnerDataDc, raw.types.PQInnerDataTemp, raw.types.PQInnerDataTempDc]


# noinspection PyRedeclaration
class PQInnerData(TLObject):  # type: ignore
    """This base type has 4 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`PQInnerData <pyrogram.raw.types.PQInnerData>`
            - :obj:`PQInnerDataDc <pyrogram.raw.types.PQInnerDataDc>`
            - :obj:`PQInnerDataTemp <pyrogram.raw.types.PQInnerDataTemp>`
            - :obj:`PQInnerDataTempDc <pyrogram.raw.types.PQInnerDataTempDc>`
    """

    QUALNAME = "pyrogram.raw.base.PQInnerData"
