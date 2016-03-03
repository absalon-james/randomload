"""This is just a playing around module. Please ignore it"""
from randomload.log import logging

import six
from six.moves.urllib import parse


from cinderclient import base

logger = logging.getLogger('randomload.actions.cinder.usage')


class Usage(base.Resource):
    def __repr__(self):
        return "<VolumeUsage>"


class UsageManager(base.ManagerWithFind):
    resource_class = Usage

    def list(self, start, end, metadata=None):
        if metadata is None:
            metadata = {}

        opts = {
            'start': start.isoformat(),
            'end': end.isoformat()
        }

        if metadata:
            opts['metadata'] = metadata

        qparams = {}
        for opt, val in opts.items():
            if val:
                if isinstance(val, six.text_type):
                    val = val.encode('utf-8')
                qparams[opt] = val

        query_string = '?%s' % parse.urlencode(qparams)
        return self._list(
            "/usages%s" % (query_string), 'tenant_usages'
        )


def usage(clients, conf, start=None, end=None, metadata=None):
    logger.info("Start: {0}".format(start))
    logger.info("End: {0}".format(end))
    logger.info("Metadata: {0}".format(metadata))

    cinder = clients.get_cinder()
    m = UsageManager(cinder)

    tenant_usages = m.list(start, end, metadata=metadata)
    for tenant_usage in tenant_usages:
        logger.info("Tenant id: {0}".format(tenant_usage.project_id))
        logger.info("Total GB Hours: {0}".format(tenant_usage.total_gb_usage))
        for usage in tenant_usage.volume_usages:
            logger.info(
                "Name: {0} - Size: {1} GB - Status: {2}".format(
                    usage['display_name'], usage['size'], usage['status']
                )
            )
