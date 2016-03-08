"""This is just a playing around module. Please ignore it"""
import datetime
import randomload.config as config

# from randomload.actions.glance import create as image_create
# from randomload.actions.glance import delete as image_delete
from randomload.actions.glance import list as image_list
from randomload.actions.glance import usage as image_usage
from randomload.args import parser as argparser
from randomload.clients import ClientManager
from randomload.log import logging

logger = logging.getLogger('randomload')
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    clients = ClientManager(
        auth_url=conf.get('auth_url'),
        username=conf.get('username'),
        password=conf.get('password'),
        project_id=conf.get('project_id')
    )

    properties = {'app_id': 'randomload'}
    logger.info(image_list(clients, conf, **properties))

    now = datetime.datetime.utcnow()

    end = now
    start = end - datetime.timedelta(days=14)
    metadata = '{"color": "red"}'
    image_usage(clients, conf, start=start, end=end, metadata=metadata)
    logger.info("\n\n")

    end = now
    start = end - datetime.timedelta(days=14)
    metadata = '{}'
    image_usage(clients, conf, start=start, end=end, metadata=metadata)
    logger.info("\n\n")

    end = now
    start = end - datetime.timedelta(days=1)
    metadata = '{"color":"green","environment":"production"}'
    image_usage(clients, conf, start=start, end=end, metadata=metadata)
    logger.info("\n\n")
