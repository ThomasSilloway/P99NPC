import argparse


class CommandlineArgs:

    def __init__(self):
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser()

        # Add arguments to the parser
        parser.add_argument("-e", "--env", help="Environment to start. Prod by default if not specified")

        # Parse the command-line arguments
        self.args = parser.parse_args()

    def get_env(self):
        env = self.args.env

        if env is None:
            env = "prod"

        return env.lower()
