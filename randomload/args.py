"""
Module for parsing arguments from the command line.

Import parser from this module.
"""
import argparse
import meta


parser = argparse.ArgumentParser(description=meta.description)

parser.add_argument(
    '--config-file', type=str,
    help="Configuration file location",
    default='/etc/randomload/randomload.yaml'
)

parser.add_argument(
    '--version', action='version',
    version='%(prog)s ' + str(meta.version)
)
