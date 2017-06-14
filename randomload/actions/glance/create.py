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

    prefix = glance_conf.get('name_prefix', 'random-image')
    name = utils.randomname(prefix=prefix)
    imagedict = utils.randomfromlist(glance_conf.get('images'))
    kwargs = {
        'name': name,
        'disk_format': imagedict.get('disk_format'),
        'container_format': imagedict.get('container_format'),
        'app_id': 'randomload'
    }
    possible_metadata = glance_conf.get('metadata', {})
    for metakey, valuelist in possible_metadata.items():
        kwargs[metakey] = utils.randomfromlist(valuelist)

    image = clients.image.images.create(**kwargs)

    clients.image.images.upload(image.id, open(imagedict.get('file'), 'rb'))
    logger.info("Created image {0}".format(image.name))
    return image
