from cinder import create as volume_create
from cinder import delete as volume_delete
from cinder import list as volume_list
from glance import create as image_create
from glance import delete as image_delete
from glance import list as image_list
from nova import create as server_create
from nova import delete as server_delete
from nova import list as server_list

ALL = {
    'image_create': image_create,
    'image_delete': image_delete,
    'image_list': image_list,
    'server_create': server_create,
    'server_delete': server_delete,
    'server_list': server_list,
    'volume_create': volume_create,
    'volume_delete': volume_delete,
    'volume_list': volume_list
}

CREATE = {
    'image_create': image_create,
    'server_create': server_create,
    'volume_create': volume_create
}

DELETE = {
    'image_delete': image_delete,
    'server_delete': server_delete,
    'volume_delete': volume_delete
}

READ = {
    'image_list': image_list,
    'server_list': server_list,
    'volume_list': volume_list
}

WRITE = {
    'image_create': image_create,
    'image_delete': image_delete,
    'server_create': server_create,
    'server_delete': server_delete,
    'volume_create': volume_create,
    'volume_delete': volume_delete
}

SETS = {
    'all': ALL,
    'create': CREATE,
    'delete': DELETE,
    'read': READ,
    'write': WRITE
}
