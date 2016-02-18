"""This is just a playing around module. Please ignore it"""
from args import parser as argparser
from clients import ClientManager
import config
import datetime
from log import logging

import six
from six.moves.urllib import parse

from novaclient import base

logger = logging.getLogger('randomload')


class Usage(base.Resource):
    def __repr__(self):
        return "<ComputeUsage>"


class AManager(base.ManagerWithFind):
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
                print "Setting {0} to {1}".format(opt, val)
                qparams[opt] = val

        query_string = '?%s' % parse.urlencode(qparams)
        print "Query string: %s" % (query_string)
        return self._list(
            "/os-complex-tenant-usage%s" % (query_string),
            "tenant_usages"
        )


def test():
    import pprint
    logger.info("Starting test...")
    args = argparser.parse_args()
    conf = config.load(args.config_file)
    clients = ClientManager(
        auth_url=conf.get('auth_url'),
        username=conf.get('username'),
        password=conf.get('password'),
        project_id=conf.get('project_id')
    )

    nova = clients.get_nova()

    servers = nova.servers.list(search_opts={"metadata": {"color": "red"}})
    for s in servers:
        print "{0} - {1}".format(s.name, s.metadata)
    exit()

    token = nova.client.get_token()
    print token

    endpoint = nova.client.get_endpoint()
    print endpoint

    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=1)

    metadata = {'fruit': 'apple', 'meat': 'yes'}

    m = AManager(nova)
    print "Start: {0}".format(start)
    print "End  : {0}".format(end)
    resp = m.list(start, end, detailed=True, metadata=metadata)
    for r in resp:
        pprint.pprint(dir(r))


if __name__ == '__main__':
    test()
