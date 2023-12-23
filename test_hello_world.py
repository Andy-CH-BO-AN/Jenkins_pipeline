import logging
import os

from dotenv import load_dotenv


def test_hello_world():
    if 'ENV' in os.environ:
        env_file = os.environ['ENV']
        load_dotenv(env_file)
    else:
        load_dotenv()

    email = os.environ.get('EMAIL')

    print(email)