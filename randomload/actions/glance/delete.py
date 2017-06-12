from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.glance.delete')


def delete(clients, conf=None):
    """Deletes a random image created by randomload.

    :param clients: randomload.clients.ClientManager
    :param conf: Dict
    """
    logger.info("Taking action delete")
    if conf is None:
        conf = {}

    image_gen = clients.image.images.list(filters={'app_id': 'randomload'})
    images = [i for i in image_gen]
    if not images:
        logger.info("Nothing to delete")
        return

    image = utils.randomfromlist(images)
    clients.image.images.delete(image.id)
    logger.info("Deleted image {0}".format(image.name))
