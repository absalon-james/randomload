"""This is just a playing around module. Please ignore it"""
import json
import six

from randomload.log import logging
from six.moves.urllib import parse

logger = logging.getLogger('randomload.actions.glance.usage')


class Controller(object):
    def __init__(self, http_client):
        self.http_client = http_client

    def list(self, start, end, detailed=False, metadata=None):
        if metadata is None:
            metadata = {}
        opts = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'detailed': int(bool(detailed))
        }

        if isinstance(metadata, dict):
            metadata = json.dumps(metadata)

        if metadata:
            opts['metadata'] = metadata

        qparams = {}
        for opt, val in opts.items():
            if val:
                if isinstance(val, six.text_type):
                    val = val.encode('utf-8')
                qparams[opt] = val

        query_string = '?%s' % parse.urlencode(qparams)
        url = '/v2/usages%s' % query_string
        return self.http_client.get(url)


def bytes_to_GB(size_in_B):
    """Return size in GB

    :param size: Numeric
    :returns: Float
    """
    return float(size_in_B) / 1024 / 1024 / 1024


def usage(clients, conf, start=None, end=None, metadata=None):
    logger.info("Start: {0}".format(start))
    logger.info("End: {0}".format(end))
    logger.info("Metadata: {0}".format(metadata))

    glance = clients.get_glance()
    controller = Controller(glance.http_client)

    resp, _ = controller.list(start, end, detailed=True, metadata=metadata)
    for tenant_usage in resp.json().get('tenant_usages', []):
        logger.info("Tenant id: {0}".format(tenant_usage.get('project_id')))
        logger.info("Total GB Hours: {0}".format(
            tenant_usage.get('total_gb_hours')
        ))
        for usage in tenant_usage.get('image_usages', []):
            logger.info(
                "Name: {0} - Size: {1} GB - Status: {2}".format(
                    usage['name'],
                    bytes_to_GB(usage['size']),
                    usage['status']
                )
            )
