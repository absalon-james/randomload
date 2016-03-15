"""This is just a playing around module. Please ignore it"""
import randomload.config as config

from randomload.actions.glance import create as image_create
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
    image_create(clients, conf)
