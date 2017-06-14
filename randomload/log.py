import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.ERROR)

logger = logging.getLogger('randomload')
logger.setLevel(logging.INFO)
