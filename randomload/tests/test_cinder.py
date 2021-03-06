"""This is just a playing around module. Please ignore it"""
import datetime
import randomload.config as config

# from randomload.actions.cinder import create as volume_create
# from randomload.actions.cinder import delete as volume_delete
from randomload.actions.cinder import list as volume_list
from randomload.actions.cinder import usage as volume_usage
from randomload.args import parser as argparser
from randomload.clients import ClientManager
from randomload.log import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger = logging.getLogger('randomload')
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    clients = ClientManager(**conf.get('auth_kwargs', {}))

    volume_list(clients, conf)

    now = datetime.datetime.utcnow()

    end = now
    start = end - datetime.timedelta(days=14)
    metadata = '{"color": "blue"}'
    volume_usage(clients, conf, start=start, end=end, metadata=metadata)
