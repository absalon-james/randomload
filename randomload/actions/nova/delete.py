from randomload import utils
from randomload.log import logging

logger = logging.getLogger('randomload.actions.nova.delete')


def delete(clients, conf=None):
    """Deletes random server.

    :param clients: randomload.clients.ClientManager
    :param conf: Dict
    """
    logger.info("Taking action delete")
    nova = clients.get_nova()
    if conf is None:
        conf = {}
    l = nova.servers.list(search_opts={'status': 'active'})
    s = utils.randomfromlist(l)
    if s:
        logger.info("Deleting {0} ...".format(s))
        nova.servers.delete(s)
    else:
        logger.info("Nothing to delete.")
