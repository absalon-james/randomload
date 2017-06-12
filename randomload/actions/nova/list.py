"""This is just a playing around module. Please ignore it"""
from randomload.log import logging

logger = logging.getLogger(__name__)


def list(clients, conf):
    logger.info("Listing active servers")
    servers = clients.compute.servers.list()
    for s in servers:
        logger.info("{0} - {1} - {2}".format(s.name, s.metadata, s.status))
