#! /usr/bin/env python
# _*_ endocing: UTF-8 _*_

"""Example: Use scan and services Methods"""

import qi
import argparse
import sys


def main(session):
    """
    This example uses the scan and services method.
    """
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. ""On robot or Local Naoqi: "
                        "use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{0}:{1}".format(args.ip, str(args.port)))
    except RuntimeError:
        print("Can't connect to Naoqi at ip {0} on port {1}.\n"
              "Please check your script arguments. Run with -h option "
              "for help.".format(args.ip, str(args.port)))
        sys.exit(1)
    main(session)
