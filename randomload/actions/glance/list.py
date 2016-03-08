"""This is just a playing around module. Please ignore it"""
from randomload.log import logging

logger = logging.getLogger('randomload.actions.glance.list')


def _property(image, prop):
    return image.get(prop, None)


def list(clients, conf, **properties):
    logger.info("Listing active images")
    glance = clients.get_glance()
    images = glance.images.list(**properties)
    for i in images:
        logger.info(
            "{0} - {1} - {2} - {3}"
            .format(
                i.name,
                _property(i, 'app_id'),
                _property(i, 'color'),
                _property(i, 'environment')
            )
        )
