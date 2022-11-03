from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()

client = SSHClient()
#LOAD HOST KEYS
#client.load_host_keys('~/.ssh/known_hosts')

client.load_host_keys('/home/wsser09/.ssh/known_hosts')
client.load_system_host_keys()

#Known_host policy
client.set_missing_host_key_policy(AutoAddPolicy())


#client.connect('10.1.1.92', username='root', password='password1')
client.connect('192.168.0.100', username='root', disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"]))
