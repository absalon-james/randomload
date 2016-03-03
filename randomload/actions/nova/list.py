"""This is just a playing around module. Please ignore it"""
from randomload.log import logging

logger = logging.getLogger('randomload.actions.nova.list')


def list(clients, conf):
    logger.info("Listing active servers")
    nova = clients.get_nova()
    servers = nova.servers.list()
    for s in servers:
        logger.info("{0} - {1} - {2}".format(s.name, s.metadata, s.status))
