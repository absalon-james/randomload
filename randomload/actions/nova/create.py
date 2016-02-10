"""Module containing action to create a nova server."""
from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.nova.create')


def create(clients, conf=None):
    """Creates server with random image and flavor.

    :param clients: randomload.clients.ClientManager
    :param conf: Configuration
    """
    logger.info("Taking action create")
    nova = clients.get_nova()
    if conf is None:
        conf = {}

    nova_conf = conf.get('nova')
    flavor = utils.randomfromlist(nova_conf.get('flavors', []))
    flavor = nova.flavors.get(flavor)
    image = utils.randomfromlist(nova_conf.get('images', []))
    name = utils.randomname()
    meta = {}
    possible_metadata = nova_conf.get('metadata', {})
    for metakey, valuelist in possible_metadata.items():
        meta[metakey] = utils.randomfromlist(valuelist)

    msg = ("Creating {0} - {1} with image {2} with metadata {3}")
    logger.info(msg.format(name, flavor, image, meta))
    nova.servers.create(name, image, flavor, meta=meta)
