from pyicloud import PyiCloudService

# this assumes that my appleid has already been added to my keyring with
# `icould --username=thornton.prime@gmail.com
api = PyiCloudService('thornton.prime@gmail.com')

for device in api.devices:
  data = device.data
  if not data['fmlyShare']:
    print(f"{data['name']}: {data['modelDisplayName']}")

