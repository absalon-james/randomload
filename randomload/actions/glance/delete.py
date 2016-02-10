from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.glance.delete')


def delete(clients, conf=None):
    """Deletes a random image created by randomload.

    :param clients: randomload.clients.ClientManager
    :param conf: Dict
    """
    logger.info("Taking action delete")
    glance = clients.get_glance()
    if conf is None:
        conf = {}

    image_gen = glance.images.list(filters={'tag': ['randomload']})
    images = [i for i in image_gen]
    if not images:
        logger.info("Nothing to delete")
        return

    image = utils.randomfromlist(images)
    glance.images.delete(image.id)
    logger.info("Deleted image {0}".format(image.name))
