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
    if conf is None:
        conf = {}

    nova_conf = conf.get('nova')
    flavor = utils.randomfromlist(nova_conf.get('flavors', []))
    flavor = clients.compute.flavors.get(flavor)
    image = utils.randomfromlist(nova_conf.get('images', []))
    name = utils.randomname(nova_conf.get('name_prefix', 'random'))
    meta = {}
    possible_metadata = nova_conf.get('metadata', {})
    for metakey, valuelist in possible_metadata.items():
        meta[metakey] = utils.randomfromlist(valuelist)

    msg = ("Creating {0} - {1} with image {2} with metadata {3}")
    logger.info(msg.format(name, flavor, image, meta))
    clients.compute.servers.create(name, image, flavor, meta=meta)
