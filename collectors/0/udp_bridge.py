#!/usr/bin/python
# This file is part of tcollector.
# Copyright (C) 2013  The tcollector Authors.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
# General Public License for more details.  You should have received a copy
# of the GNU Lesser General Public License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.
"""Listens on a local UDP socket for incoming Metrics """

import socket
import sys
from collectors.lib import utils

HOST = '127.0.0.1'
PORT = 8953
SIZE = 8192
TIMEOUT = 1

def main():
    utils.drop_privileges()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((HOST, PORT))
    except socket.error as msg:
        sys.stderr.write('could not open socket: %s\n' % msg)
        sys.exit(1)

    try:
        while 1:
            data, address = sock.recvfrom(SIZE)
            if not data:
                sys.stderr.write("invalid data\n")
                break
            print data
    except KeyboardInterrupt:
        sys.stderr.write("keyboard interrupt, exiting\n")
    finally:
        sock.close()

if __name__ == "__main__":
    main()

sys.exit(0)