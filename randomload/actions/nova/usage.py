"""This is just a playing around module. Please ignore it"""
from randomload.log import logging

import six
from six.moves.urllib import parse

from novaclient import base

logger = logging.getLogger('randomload.actions.nova.usage')


class Usage(base.Resource):
    def __repr__(self):
        return "<ComputeUsage>"


class UsageManager(base.ManagerWithFind):
    resource_class = Usage

    def list(self, start, end, detailed=False, metadata=None):
        if metadata is None:
            metadata = {}

        opts = {
            'start': start.isoformat(),
            'end': end.isoformat(),
            'detailed': int(bool(detailed))
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
            "/os-complex-tenant-usage%s" % (query_string),
            "tenant_usages"
        )


def usage(clients, conf, start=None, end=None, metadata=None):
    logger.info("Start: {0}".format(start))
    logger.info("End: {0}".format(end))
    logger.info("Metadata: {0}".format(metadata))

    nova = clients.get_nova()
    m = UsageManager(nova)
    resp = m.list(start, end, detailed=True, metadata=metadata)
    for r in resp:
        logger.info("Total hours: {0}".format(r.total_hours))
        logger.info("Total local GB Hours: {0}".format(r.total_local_gb_usage))
        logger.info("Total memory MB Hours: {0}"
                    .format(r.total_memory_mb_usage))
        logger.info("Total vcpu hours: {0}".format(r.total_vcpus_usage))
        for s in r.server_usages:
            logger.info("{0} - {1} - {2}".format(
                s.get('name'),
                s.get('flavor'),
                s.get('state')
            ))
