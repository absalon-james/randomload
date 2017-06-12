from log import logging
from osc_lib import clientmanager
from os_client_config import config as cloud_config
from openstackclient.common.clientmanager import PLUGIN_MODULES

logger = logging.getLogger('randomload.clients')


class _ClientManager:

    def __init__(self):
        self._instance = None

    def __call__(self):
        """Get an instance of the openstack client manager.

        :returns: Instance of client manager
        :rtype: osc_lib.clientmanager.ClientManager
        """
        if self._instance is None:
            cc = cloud_config.OpenStackConfig()
            cloud = cc.get_one_cloud()
            api_version = {}
            for mod in PLUGIN_MODULES:
                default_version = getattr(mod, 'DEFAULT_API_VERSION', None)
                version_opt = str(default_version)
                if version_opt:
                    api = mod.API_NAME
                    api_version[api] = version_opt

            api_version['image'] = '2'

            cm = clientmanager.ClientManager(
                cli_options=cloud,
                api_version=api_version
            )
            cm.setup_auth()
            self._instance = cm
        return self._instance


clients = _ClientManager()
