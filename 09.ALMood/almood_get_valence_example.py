#! /usr/bin/env python
# _*_ encoding: UTF-8 _*_

"""Example: Use currentPersonState Method"""

import qi
import argparse
import sys
import time


def main(session):
    """
    This example uses the currentPersonState method.
    """
    # Get the service ALMood.
    moodService = session.service("ALMood")

    moodService.subscribe("Tutorial_GetValence", "Active")
    # The preloading of all ALMood extractors may take up to 3 seconds:
    time.sleep(3)
    print moodService.currentPersonState()["valence"]["value"]

    moodService.unsubscribe("Tutorial_GetValence")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{0}:{1}".format(args.ip, str(args.port)))
    except RuntimeError as e:
        print("Can't connect to Naoqi at ip {0} on port {1}.\n"
              "Please check your script arguments. Run with -h option for help."
              "".format(args.ip, str(args.port)))
        sys.exit(1)
    main(session)
