import logging
import os


def test_hello_world():
    env_file = os.environ
    logging.info(env_file)