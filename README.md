# randomload

## Installation
```shell
git clone https://github.com/absalon-james/randomload.git
cd randomload
python setup.py install
```

## Configuration
The default location for the randomload yaml configuration is /etc/randomload/randomload.yaml.
This can be changed with the command line argument '--config-file'.

```yaml
# Usually something like http://some-ip:5000/v2.0
auth_url: http://some-ip:5000/v2.0

# Openstack username
username: yourusername

# Openstack password
password: yourpassword

# Openstack project or tenant id
project_id: your_tenant_or_project_id

# Time in seconds between each action
interval: 60

nova:
  # List of images to choose from. Listed by uuid
  images:
    - aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    - bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb

  # List of flavors to choose from. Listed by flavor id
  flavors:
    - '1'
    - '2'

  # Dictionary of possible key value pairs for instance metadata
  metadata:
    color:
      - red
      - blue
      - green
    environment:
      - dev
      - test
      - production

glance:
  # Describe images to be uploaded to glance
  images:
    - file: /etc/randomload/images/cirros-0.3.4-x86_64-disk.img
      disk_format: qcow2
      container_format: bare

  # Randomload will sample tags from this list
  tags:
    - banana
    - orange
    - apple
    - pear
    - grape
    - forty
```
