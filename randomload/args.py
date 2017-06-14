import argparse
import actions

description = (
    "Simple tool for consuming random resources in an openstack cloud."
)


parser = argparse.ArgumentParser(
    prog='randomload',
    description=description
)

parser.add_argument(
    '--config-file',
    type=str,
    help="Configuration file location.",
    default='/etc/randomload/randomload.yaml'
)

parser.add_argument(
    '--action-set',
    type=str,
    choices=actions.SETS.keys(),
    help="Set of actions. Defaults to all actions.",
    default='all'
)

parser.add_argument(
    '--action',
    action="append",
    type=str,
    choices=actions.ALL.keys(),
    default=[],
    help=("Provide a list of random actions to perform. Defaults to all."
          "Can be provided multiple times.")
)

parser.add_argument(
    '--debug',
    action='store_true',
    default=False,
    help="Set log level to debug."
)
