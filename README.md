# nandy

## Installation
```shell
git clone https://github.com/absalon-james/randomload.git
cd randomload
python setup.py install

## Configuration
The default location for the nandy yaml configuration is /etc/randomload/randomload.yaml.
This can be changed with the command line argument '--config-file'.

```yaml
# Usually something like http://some-ip:5000/v2.0
auth_url: http://your_auth_url

# Openstack username
username: some_username

# Openstack password
password: some_password

# Openstack tenant uuid
project_id: some_tenant_id


# Time in seconds between each random action.
interval: 60

# List of images to choose from. Listed by uuid
images:
  - aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
  - bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb

# List of flavors to choose from. Listed by flavor id
flavors:
  - '1'
  - '2'

```
