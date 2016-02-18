from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.cinder.delete')


def delete(clients, conf=None):
    """Deletes random server.

    :param clients: randomload.clients.ClientManager
    :param conf: Dict
    """
    logger.info("Taking action delete")
    cinder = clients.get_cinder()
    if conf is None:
        conf = {}

    search_opts = {
        'metadata': {
            'app': 'randomload'
        },
        'status': 'available'
    }
    volumes = cinder.volumes.list(search_opts=search_opts)
    if not volumes:
        logger.info("Nothing to delete.")
    else:
        volume = utils.randomfromlist(volumes)
        cinder.volumes.delete(volume)
        logger.info("Deleted volume {0} - {1} - {2}"
                    .format(volume.name, volume.size, volume.metadata))
