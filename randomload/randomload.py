from args import parser as argparser
import config
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as novaclient
import random
import time


def get_nova(auth_url=None, username=None, password=None, project_id=None):
    """Get nova client.

    :param auth_url: String keystone auth url
    :param username: String openstack username
    :param password: String openstack password
    :param project_id: String project_id - Tenant uuid
    :returns: novaclient.client.Client
    """
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(
        auth_url=auth_url,
        username=username,
        password=password,
        project_id=project_id
    )
    sess = session.Session(auth=auth)
    return novaclient.Client('2.1', session=sess)


def randomname(prefix='random', l=6):
    """Generates random string name of hexadecimal characters.

    :param prefix: String to preprend to name
    :param l: Length of generated name.
    :returns: String
    """
    r = ''.join(random.choice('0123456789ABCDEF') for i in xrange(l))
    return '{0}-{1}'.format(prefix, r)


def randomfromlist(l):
    """Returns random item from list.

    :param l: List
    :returns: object|None
    """
    if not l:
        return None
    return l[random.randrange(len(l))]


def action_create(nova, **kwargs):
    """Creates server with random image and flavor.

    :param nova: Nova client instance
    :param flavors: List of flavors to choose from
    :param images: List of images to choose from
    """
    flavor = randomfromlist(kwargs.get('flavors', []))
    flavor = nova.flavors.get(flavor)
    image = randomfromlist(kwargs.get('images', []))
    name = randomname()
    print("Creating {0} - {1} with image {2}".format(name, flavor, image))
    nova.servers.create(name, image, flavor)


def action_delete(nova, **kwargs):
    """Deletes random server.

    :param nova: Nova client instance
    """
    l = nova.servers.list(search_opts={'status': 'active'})
    s = randomfromlist(l)
    if s:
        print "Deleting {0} ...".format(s)
        nova.servers.delete(s)
    else:
        print "Nothing to delete."

actions = [action_create, action_delete]

if __name__ == '__main__':
    args = argparser.parse_args()
    conf = config.load(args.config_file)

    nova = get_nova(
        auth_url=conf.get('auth_url'),
        username=conf.get('username'),
        password=conf.get('password'),
        project_id=conf.get('project_id')
    )
    images = conf.get('images', [])
    flavors = conf.get('flavors', [])
    interval = conf.get('interval', 60)

    last_action_time = 0
    while True:
        now = time.time()
        if now - last_action_time > interval:
            action = randomfromlist(actions)
            try:
                action(nova, images=images, flavors=flavors)
            except Exception as e:
                print e
            last_action_time = time.time()
        time.sleep(1)
