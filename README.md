# tyger-discord-webhooks.py
An unofficial library for discord webhooks

<h2>By <a href="https://tyger375.tk/">tyger 375#4141</a></h2>

**requires <a href="https://pypi.org/project/requests/">requests</a> and <a href="https://pypi.org/project/jsons/">JSON</a> modules installed**

Login to the webhook:

```py
from tyger_discord import *

webhook = Webhook()
webhook.login("token", "server_id")
```

Send a message

```py
async def Start():
  #All the functions are in async
  await webhook.send("content", embeds=[])
  
asyncio.run(Start())
```

Create an Embed
```py
Embed = Embed(title="title", description="description")
#You can also use Embed.description = "description" or Embed.title = "title"
Embed.add_field(name="field", value="value")
Embed.set_thumbnail("url)
Embed.set_image("url")
Embed.set_author("text", icon_url="icon_url", url="url")
Embed.set_footer(text="text", icon_url="icon_url")
```
