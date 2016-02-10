from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.glance.create')


def create(clients, conf=None):
    """Creates a glance image

    :param clients: randomload.clients.Clientmanager
    :param conf: Dict
    """
    logger.info("Taking action image_create")
    if conf is None:
        conf = {}
    glance_conf = conf.get('glance', {})
    glance = clients.get_glance()

    name = utils.randomname(prefix='random-image')
    imagedict = utils.randomfromlist(glance_conf.get('images'))

    image = glance.images.create(
        name=name,
        disk_format=imagedict.get('disk_format'),
        container_format=imagedict.get('container_format')
    )

    glance.images.upload(image.id, open(imagedict.get('file'), 'rb'))

    # Add a tag to identify image as one created by randomload
    tag = 'randomload'
    glance.image_tags.update(image.id, 'randomload')

    # Randomly sample from available random tags
    extra_tags = utils.randomsample(glance_conf.get('tags', []), 2)
    for t in extra_tags:
        glance.image_tags.update(image.id, t)

    logger.info(
        "Created image {0} with tags {1}"
        .format(image.name, extra_tags + ['randomload'])
    )
