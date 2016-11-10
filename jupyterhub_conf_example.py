c = get_config()
import logging
c.JupyterHub.log_level = logging.DEBUG
c.JupyterHub.base_url = '/app/notebooks'
c.JupyterHub.hub_port = 8081
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.proxy_api_ip = '0.0.0.0'
c.JupyterHub.spawner_class = 'libcloudspawner.spawner.libcloudSpawner'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.proxy_auth_token = '8864d13d72822339c3cbe2347eba6be9f97bb430e1c85bb18280bc7baec77dcd'
c.JupyterHub.cookie_secret = bytes.fromhex('8864d13d72822339c3cbe2347eba6be9f97bb430e1c85bb18280bc7baec7aaaaadcd')
c.Spawner.start_timeout = 90
c.Spawner.http_timeout = 60
c.Spawner.debug = False
c.Spawner.notebook_dir = '~/'
c.Spawner.args = ['']
c.LibcloudSpawner.cloud_url = "https://KEYSTONE_API/v3/auth/tokens"
c.LibcloudSpawner.cloud_user = "jupyter"
c.LibcloudSpawner.cloud_userpassword = "secret"
c.LibcloudSpawner.cloud_project = "jupyterproject"
c.LibcloudSpawner.machine_sizes = [("1vcpu 2Go RAM", "m1.small"), ("4vcpu 8Go RAM", "m1.large")]
c.LibcloudSpawner.machine_images = [("Default image","jpysingleuser-general-applayer")]
c.LibcloudSpawner.machine_image = "notebook-machine-template"
c.LibcloudSpawner.machine_net = "ext-net"
c.LibcloudSpawner.notebookargs = "--notebook-dir=~"
