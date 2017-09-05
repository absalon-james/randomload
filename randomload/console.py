import actions
import config
import time
import utils
from args import parser
from clients import clients as openstack_clients
from log import logging

logger = logging.getLogger('randomload')


def load_actions(action_set, chosen_actions):
    """Assemble a list of actions that will be randomly chosen from.

    Step 1 is to get a set of actions.
    These will be all, create, delete, read, write.
    Step 2 is to only include the chosen actions from the set of actions.
    If no chosen actions are provided, then return all of the action set.

    :param action_set: Name of an action set. (all, create, ...)
    :type action_set: str
    :param chosen_actions: List of explicitly chosen actions.
    :type chosen_actions: list
    :return: List of action function objects.
    :rtype: list
    """
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
    """Main loop of the console script.

    At each interval, choose a random action.
    CTRL + C should break it.
    """
    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

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
