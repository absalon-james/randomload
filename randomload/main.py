from args import parser as argparser
from clients import ClientManager
import config
from keystoneauth1 import loading
from keystoneauth1 import session
from log import logging
from novaclient import client as novaclient
import time
import utils

from actions.nova import delete as server_delete
from actions.nova import create as server_create
from actions.glance import create as image_create
from actions.glance import delete as image_delete

logger = logging.getLogger('randomload')


def get_nova(auth_url=None, username=None, password=None, project_id=None):
    """Get nova client.

    :param auth_url: String keystone auth url
    :param username: String openstack username
    :param password: String openstack password
    :param project_id: String project_id - Tenant uuid
    :returns: novaclient.client.Client
    """
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(
        auth_url=auth_url,
        username=username,
        password=password,
        project_id=project_id
    )
    sess = session.Session(auth=auth)
    return novaclient.Client('2.1', session=sess)


def run():
    logger.info("Starting randomload...")
    actions = [server_create, server_delete, image_create, image_delete]
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    interval = conf.get('interval', 60)

    clients = ClientManager(
        auth_url=conf.get('auth_url'),
        username=conf.get('username'),
        password=conf.get('password'),
        project_id=conf.get('project_id')
    )

    last_action_time = 0
    while True:
        now = time.time()
        if now - last_action_time > interval:
            action = utils.randomfromlist(actions)
            try:
                action(clients, conf=conf)
            except Exception as e:
                print e
            last_action_time = time.time()
        time.sleep(1)


def test():
    logger.info("Starting test...")
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    clients = ClientManager(
        auth_url=conf.get('auth_url'),
        username=conf.get('username'),
        password=conf.get('password'),
        project_id=conf.get('project_id')
    )
    image_delete(clients, conf)

if __name__ == '__main__':
    run()
