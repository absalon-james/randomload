"""This is just a playing around module. Please ignore it"""
from randomload.log import logging

logger = logging.getLogger('randomload.actions.cinder.list')


def list(clients, conf):
    logger.info("Listing active volumes")
    volumes = clients.volume.volumes.list()
    for v in volumes:
        logger.info("{0} - {1}".format(v.name, v.metadata))
    return volumes
