#! /usr/bin/env python
# _*_ encoding: UTF-8 _*_

"""Example: Use ALKnowledge Module"""

import qi
import argparse
import sys


def main(session):
    """
    This example uses ALKnowledge module.
    """
    # Get the service ALKnowledge.
    knowledge_service = session.service("ALKnowledge")

    # Add triplets to the ontology
    knowledge_service.add("tutorial", "sky", "hasColor", "blue")
    knowledge_service.add("tutorial", "smurf", "hasColor", "blue")
    knowledge_service.add("tutorial", "smurf", "hasColor", "white")

    # Get subjects
    result = knowledge_service.getSubject("tutorial", "hasColor", "blue")
    print result  # Should print ['sky', 'smurf']

    # Get predicates
    result = knowledge_service.getPredicate("tutorial", "sky", "blue")
    print result  # Should print ['hasColor']

    # Get objects
    result = knowledge_service.getObject("tutorial", "smurf", "hasColor")
    print result  # Should print ['blue', 'white']

    # Update
    result = knowledge_service.Update("tutorial", "smurf", "hasColor", "red")
    result = knowledge_service.getObject("tutorial", "smurf", "hasColor")
    print result  # Should print ['red']

    # Contains
    result = knowledge_service.contains("tutorial", "smurf", "hasColor", "red")
    print result  # Should print True

    # Remove
    result = knowledge_service.remove("tutorial", "smurf", "hasColor", "red")
    result = knowledge_service.contains("tutorial", "smurf", "hasColor", "red")
    print result  # Should print False

    # Query
    result = knowledge_service.query("tutorial", "sky", "hasColor", "?")
    print result  # Should print ['blue']

    # Reset knowledge
    result = knowledge_service.resetKnowledge("tutorial")


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
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"{0}\" on port {1}.\n"
              "Please check your script arguments. Run with -h option of help."
              "".format(args.ip, str(args.port)))
        sys.exit(1)
    main(session)
