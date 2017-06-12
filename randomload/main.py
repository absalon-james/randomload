from args import parser as argparser
from clients import clients as openstack_clients
import config
from log import logging
import time
import utils

from actions.cinder import create as volume_create
from actions.cinder import delete as volume_delete
from actions.glance import create as image_create
from actions.glance import delete as image_delete
from actions.nova import delete as server_delete
from actions.nova import create as server_create

logger = logging.getLogger('randomload')


def run():
    logger.info("Starting randomload...")
    actions = [
        server_create,
        server_delete,
        image_create,
        image_delete,
        volume_create,
        volume_delete,
    ]
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    interval = conf.get('interval', 60)

    clients = openstack_clients()

    last_action_time = 0
    while True:
        now = time.time()
        if now - last_action_time > interval:
            action = utils.randomfromlist(actions)
            try:
                action(clients, conf=conf)
            except Exception:
                logger.exception("Unable to perform action:")
            last_action_time = time.time()
        time.sleep(1)


if __name__ == '__main__':
    run()
