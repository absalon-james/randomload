from keystoneauth1 import loading
from keystoneauth1 import session
from cinderclient import client as cinderclient
from novaclient import client as novaclient
from glanceclient import Client as glanceclient


class ClientManager(object):
    """Object that manages multiple openstack clients.

    Operates with the intention of sharing one keystone auth session.
    """
    def __init__(self, **auth_kwargs):
        """Inits the client manager.

        :param auth_url: String keystone auth url
        :param username: String openstack username
        :param password: String openstack password
        :param project_id: String project_id - Tenant uuid
        """
        self.session = None
        self.nova = None
        self.glance = None
        self.cinder = None
        self.auth_kwargs = auth_kwargs

    def get_session(self):
        """Get a keystone auth session.

        :returns: keystoneauth1.session.Session
        """
        if self.session is None:
            loader = loading.get_plugin_loader('password')
            auth = loader.load_from_options(**self.auth_kwargs)
            self.session = session.Session(auth=auth)
        return self.session

    def get_nova(self, version='2.1'):
        """Get a nova client instance.

        :param version: String api version
        :returns: novaclient.client.Client
        """
        if self.nova is None:
            self.nova = novaclient.Client(version, session=self.get_session())
        return self.nova

    def get_glance(self, version='2'):
        """Get a glance client instance.

        :param version: String api version
        :return: glanceclient.Client
        """
        if self.glance is None:
            self.glance = glanceclient(version, session=self.get_session())
        return self.glance

    def get_cinder(self, version='2'):
        """Get a cinder client instance.

        :param version: String api version
        :return: cinderclient.client.Client
        """
        if self.cinder is None:
            self.cinder = cinderclient.Client(version,
                                              session=self.get_session())
        return self.cinder
