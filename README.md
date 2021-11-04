# tyger-discord.py
An unofficial library for discord webhooks

requires requests and json modules

Login to the webhook:

```
from tyger_discord import *

webhook = Webhook()
webhook.login("token", "server_id")
```
