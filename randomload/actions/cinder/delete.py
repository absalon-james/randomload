from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.cinder.delete')


def delete(clients, conf=None):
    """Deletes random server.

    :param clients: randomload.clients.ClientManager
    :param conf: Dict
    """
    logger.info("Taking action delete")
    if conf is None:
        conf = {}

    search_opts = {
        'metadata': {
            'app': 'randomload'
        },
        'status': 'available'
    }
    volumes = clients.volume.volumes.list(search_opts=search_opts)
    if not volumes:
        logger.info("Nothing to delete.")
    else:
        volume = utils.randomfromlist(volumes)
        clients.volume.volumes.delete(volume)
        logger.info("Deleted volume {0} - {1} - {2}"
                    .format(volume.name, volume.size, volume.metadata))
