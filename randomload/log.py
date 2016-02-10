import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

logger = logging.getLogger('randomload')
logger.setLevel(logging.DEBUG)
