import sys
import os

sys.path.insert(0, os.getcwd())

from urban.urban_api import (
    apply_word_to_url,
    send_exists_request,
    send_phrase_request,
)
