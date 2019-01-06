#! /usr/bin/env python
"""Nintendo DLS1 client

    Copyright (C) 2019 Sepalani

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import base64
import requests

DLS1_SERVER = "http://dls1.nintendowifi.net"


class Client(object):
    """DLS1 Client class."""

    def __init__(self, url=DLS1_SERVER, options={}, headers={}):
        self.url = url + "/download"
        self.headers = headers
        self.options = options

    def game(self, gamecd, rhgamecd=None):
        """Set game to download DLC from."""
        self.options["gamecd"] = gamecd
        self.options["rhgamecd"] = rhgamecd or gamecd

    def send(self, **kwargs):
        post_data = {k: v for k, v in self.options.items()}
        post_data.update(kwargs)
        return requests.post(
            self.url, headers=self.headers, data={
            k: base64.b64encode(v).replace("=", "*")
            for k, v in post_data.items()
        })

    def list(self, **kwargs):
        return self.send(action="list", **kwargs)

    def count(self, **kwargs):
        return self.send(action="count", **kwargs)

    def contents(self, **kwargs):
        return self.send(action="contents", **kwargs)


if __name__ == "__main__":
    pass
