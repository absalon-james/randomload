"""Module containing action to create a cinder volume."""
from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.cinder.create')


def create(clients, conf=None):
    """Creates server with random image and flavor.

    :param clients: randomload.clients.ClientManager
    :param conf: Configuration
    """
    logger.info("Taking action create")
    if conf is None:
        conf = {}
    cinderconf = conf.get('cinder', {})

    name = utils.randomname(prefix='random-volume')
    size = utils.randomfromlist(cinderconf.get('sizes', [1]))

    meta = {'app': 'randomload'}
    possible_metadata = cinderconf.get('metadata', {})
    for metakey, valuelist in possible_metadata.items():
        meta[metakey] = utils.randomfromlist(valuelist)

    volume = clients.volume.volumes.create(name=name, size=size, metadata=meta)
    logger.info("Created volume {0} with metadata {1}"
                .format(volume.name, volume.metadata))
    return volume
