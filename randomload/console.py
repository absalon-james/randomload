import actions
import config
import time
import utils
from args import parser
from clients import clients as openstack_clients
from log import logging

logger = logging.getLogger('randomload')


def load_actions(action_set, chosen_actions):

    action_set = actions.SETS.get(action_set)
    if chosen_actions:
        action_set = {
            name: action for name, action in action_set.items()
            if name in chosen_actions
        }
    logger.debug(
        "Using only the following actions: {}"
        .format(action_set.keys())
    )
    return action_set.values()


def run():
    args = parser.parse_args()
    logger.debug("Using configuration file: {}".format(args.config_file))
    logger.debug("Using action set: {}".format(args.action_set))

    actions = load_actions(args.action_set, args.action)
    conf = config.load(args.config_file)
    interval = conf.get('interval', 60)

    clients = openstack_clients()
    last_action_time = 0

    try:
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
    except KeyboardInterrupt:
        logger.info("Exiting...")

if __name__ == '__main__':
    run()
