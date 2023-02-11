import logging

from src.app.app import App
from src.app.app_logger import AppLogger
from src.app.commandline_args import CommandlineArgs
from src.app.config import Config

logger = AppLogger()
logger.configure()

commandline_args = CommandlineArgs()

env = commandline_args.get_env()
logging.info(f"Loading environment: {env}")

config = Config(env)


def main():
    logging.info("Starting main thread")
    app = App()
    app.run()

try:
    main()
except KeyboardInterrupt:
    logging.info("Shutting down from keyboard interrupt")
