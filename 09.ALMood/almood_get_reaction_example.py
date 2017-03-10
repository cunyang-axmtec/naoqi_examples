#! /usr/bin/env python
# _*_ encoding:UTF-8 _*_

"""Example: Use getEmotionalReaction method"""

import qi
import argparse
import sys
import time


def main(session):
    """
    This example uses the getEmotionalReaction method.
    """
    # Get the services ALMood and ALTextToSpeech.
    moodService = session.service("ALMood")
    tts = session.service("ALTextToSpeech")
    moodService.subscribe("Tutorial_RecordMood", "Active")
    # The preloading of all ALMood extractors may take up to 2 seconds:
    time.sleep(2)

    # The robot tries to provocate an emotioin by greeting you
    tts.say("You look great today!")
    # The robot will try to analysis your reactioin during the next 3 seconds
    print moodService.getEmotionalReaction()

    moodService.unsubscribe("Tutorial_RecordMood")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{0}:{1}".format(args.ip, str(args.port)))
    except RuntimeError:
        print("Can't connect to Naoqi at ip {0} on port {1}.\n"
              "Please check your script arguments. Run with -h option for help."
              "".format(args.ip, str(args.port)))
        sys.exit(1)
    main(session)
