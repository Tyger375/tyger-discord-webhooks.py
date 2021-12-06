# tyger-discord.py
An unofficial library for discord webhooks

<h2>By <a href="https://tyger375.tk/">tyger 375#4141</a></h2>

**requires requests and json modules**

Login to the webhook:

```
from tyger_discord import *

webhook = Webhook()
webhook.login("token", "server_id")
```

Send a message

```
async def Start():
  #All the functions are in async
  await webhook.send("content", embeds=[])
  
asyncio.run(Start())
```

Create an Embed
```
Embed = Embed(title="title", description="description")
#You can also use Embed.description = "description" or Embed.title = "title"
Embed.add_field(name="field", value="value")
Embed.set_thumbnail("url)
Embed.set_image("url")
Embed.set_author("text", icon_url="icon_url", url="url")
Embed.set_footer(text="text", icon_url="icon_url")
```
