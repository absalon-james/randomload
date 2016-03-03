"""This is just a playing around module. Please ignore it"""
import datetime
import randomload.config as config

# from randomload.actions.nova import create as server_create
# from randomload.actions.nova import delete as server_delete
from randomload.actions.nova import list as server_list
from randomload.actions.nova import usage as server_usage
from randomload.args import parser as argparser
from randomload.clients import ClientManager
from randomload.log import logging

logger = logging.getLogger('randomload')

if __name__ == '__main__':
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    clients = ClientManager(
        auth_url=conf.get('auth_url'),
        username=conf.get('username'),
        password=conf.get('password'),
        project_id=conf.get('project_id')
    )

    server_list(clients, conf)

    now = datetime.datetime.utcnow()

    end = now
    start = end - datetime.timedelta(days=14)
    metadata = '{"color": "red"}'
    server_usage(clients, conf, start=start, end=end, metadata=metadata)

    end = now
    start = end - datetime.timedelta(days=14)
    metadata = '{}'
    server_usage(clients, conf, start=start, end=end, metadata=metadata)

    end = now
    start = end - datetime.timedelta(days=1)
    metadata = '{"color":"green","environment":"production"}'
    server_usage(clients, conf, start=start, end=end, metadata=metadata)
