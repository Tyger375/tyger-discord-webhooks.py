import asyncio
import requests
import json as JSON

class Webhook():
    def __init__(self):
        self.token = None
        self.serverId = None
        pass

    def __repr__(self):
        return f"<DiscordWebhook {self.token}>"
    
    def login(self, token, server):
        richiesta = requests.post("https://discord.com/api/webhooks/" + str(server) + "/" + str(token))
        response = richiesta.json()
        if "message" in response:
            raise Exception(response["message"])
        self.token = token
        self.serverId = server
    
    async def send(self, content="", **kwargs):
        if self.token == None:
            raise Exception("Non hai fatto il login al webhook")
        message = content
        embeds = kwargs.get("embeds", None)
        global richiesta
        headers = {"Content-Type":"application/json"}
        if embeds != None:
            if type(embeds) is list:
                tuttiEmbeds = []
                for embed in embeds:
                    tuttiEmbeds.append(embed.to_dict())
                if tuttiEmbeds == []:
                    data = {
                        "content":message,
                    }
                    richiesta = requests.post(
                        "https://discord.com/api/webhooks/" + str(self.serverId) + "/" + str(self.token), 
                        data=JSON.dumps(data),
                        params={"wait":True},
                        headers=headers
                    )
                else:
                    data = {
                        "content":message,
                        "embeds":tuttiEmbeds
                    }
                    richiesta = requests.post(
                        "https://discord.com/api/webhooks/" + str(self.serverId) + "/" + str(self.token), 
                        data=JSON.dumps(data),
                        params={"wait":True},
                        headers=headers
                    )
            else:
                try:
                    EMBED = [embeds.to_dict()]
                except Exception as errore:
                    raise Exception(str(errore))
                data = {
                    "content":message,
                    "embeds":EMBED
                }
                richiesta = requests.post(
                    "https://discord.com/api/webhooks/" + str(self.serverId) + "/" + str(self.token), 
                    data=JSON.dumps(data), 
                    params={"wait":True}, 
                    headers=headers
                )
        else:
            data2={
                "content":message,
            }
            richiesta = requests.post("https://discord.com/api/webhooks/" + str(self.serverId) + "/" + str(self.token), 
                data=JSON.dumps(data2),
                headers=headers,
                params={"wait":True}
            )
        #print(richiesta.text)
        toJson = richiesta.json()
        Messaggio = Message(toJson["id"], toJson["content"], toJson["type"], toJson["embeds"], toJson["pinned"], toJson["mentions"], toJson["mention_roles"], toJson["attachments"], toJson["mention_everyone"], toJson["tts"], toJson["timestamp"], toJson["edited_timestamp"], toJson["flags"], toJson["components"], self.token, self.serverId)
        return Messaggio
    
    async def getMessage(self, messageId):
        if self.token == None:
            raise Exception("Non hai fatto il login al webhook")
        richiesta = requests.get(
            f"https://discord.com/api/webhooks/{self.serverId}/{self.token}/messages/{messageId}",
        )
        toJson = richiesta.json()
        if "message" in toJson:
            raise Exception(toJson["message"])
        Messaggio = Message(toJson["id"], toJson["content"], toJson["type"], toJson["embeds"], toJson["pinned"], toJson["mentions"], toJson["mention_roles"], toJson["attachments"], toJson["mention_everyone"], toJson["tts"], toJson["timestamp"], toJson["edited_timestamp"], toJson["flags"], toJson["components"], self.token, self.serverId)
        return Messaggio
class Message():
    def __init__(self, id, content, type, embeds, pinned, mentions, mention_roles, attachments, mention_everyone, tts, timestamp, edited_timestamp, flags, components, webhook_token, webhook_id):
        self.id = id
        self.content = content
        self.type = type
        self.embeds = embeds
        self.pinned = pinned
        self.mentions = mentions
        self.mention_roles = mention_roles
        self.attachments = attachments
        self.mention_everyone = mention_everyone
        self.tts = tts
        self.timestamp = timestamp
        self.edited_timestamp = edited_timestamp
        self.flags = flags
        self.components = components
        self.webhook_token = webhook_token
        self.webhook_id = webhook_id

    def __repr__(self):
        return f"<DiscordMessage {self.id}>"

    async def edit(self, content, **kwargs):
        embeds = kwargs.get("embeds", None)
        headers = {
            "Content-Type":"application/json"
        }
        if embeds == None:
            requests.patch(f"https://discord.com/api/webhooks/{self.webhook_id}/{self.webhook_token}/messages/{self.id}", data={
                "content":content
            }, params={"wait":True})
        else:
            if type(embeds) is list:
                tuttiEmbeds = []
                for embed in embeds:
                    tuttiEmbeds.append(embed.to_dict())
                if tuttiEmbeds == []:
                    data = {
                        "content":content,
                    }
                    richiesta = requests.patch(
                        f"https://discord.com/api/webhooks/{str(self.webhook_id)}/{self.webhook_token}/messages/{self.id}" + str(self.token), 
                        data=JSON.dumps(data),
                        params={"wait":True},
                        headers=headers
                    )
                else:
                    data = {
                        "content":content,
                        "embeds":tuttiEmbeds
                    }
                    richiesta = requests.patch(
                        f"https://discord.com/api/webhooks/{str(self.webhook_id)}/{str(self.webhook_token)}/messages/{self.id}", 
                        data=JSON.dumps(data),
                        params={"wait":True},
                        headers=headers
                    )
            else:
                try:
                    EMBED = [embeds.to_dict()]
                except Exception as errore:
                    raise Exception(str(errore))
                data = {
                    "content":content,
                    "embeds":EMBED
                }
                richiesta = requests.patch(
                    f"https://discord.com/api/webhooks/{str(self.webhook_id)}/{str(self.webhook_token)}/messages/{self.id}", 
                    data=JSON.dumps(data), 
                    params={"wait":True}, 
                    headers=headers
                )

    async def delete(self):
        richiesta = requests.delete(
            f"https://discord.com/api/webhooks/{self.webhook_id}/{self.webhook_token}/messages/{self.id}"
        )
        return richiesta

    def to_dict(self):
        Obj = {
            "id": self.id,
            "content":self.content,
            "type":self.type,
            "embeds":self.embeds,
            "pinned":self.pinned,
            "mentions":self.mentions,
            "mention_roles":self.mention_roles,
            "attachments":self.attachments,
            "mention_everyone":self.mention_everyone,
            "tts":self.tts,
            "timestamp":self.timestamp,
            "edited_timestamp":self.edited_timestamp,
            "flags":self.flags,
            "components":self.components,
            "webhook_token":self.webhook_token,
            "webhook_id":self.webhook_id,
        }
        return Obj
class Embed():
    def __init__(self, title="undefined", description="undefined", color=0):
        self.title = title
        self.description = description
        self.color = color
        self.fields = []
        self.footer = {}
        self.thumbnail = {}
        self.image = {}
        self.author = {}

    def to_dict(self):
        embed = {}
        embed["title"] = self.title
        embed["description"] = self.description
        embed["color"] = self.color
        embed["fields"] = self.fields
        embed["footer"] = self.footer
        embed["thumbnail"] = self.thumbnail
        embed["image"] = self.image
        embed["author"] = self.author
        return embed

    def add_field(self, value="undefined", name="undefined", inline=False):
        Field = {}
        Field["name"] = name
        Field["value"] = value
        Field["inline"] = inline
        self.fields.append(Field)

    def set_footer(self, text="undefined", icon_url="undefined"):
        footer = {}
        footer["text"] = text
        if icon_url != "undefined":
            footer["icon_url"] = icon_url
        self.footer = footer

    def set_thumbnail(self, url):
        thumbnail = {
            "url":url
        }
        self.thumbnail = thumbnail

    def set_image(self, url):
        image = {
            "url":url
        }
        self.image = image

    def set_author(self, name, url=None, icon_url=None):
        author = {}
        author["name"] = name
        if url != None:
            author["url"] = url
        if icon_url != None:
            author["icon_url"] = icon_url
        self.author = author
class EmbedColor():
    def __init__(self) -> None:
        pass

    def red():
        return 0xe74c3c
    
    def dark_red():
        return 0x992d22

    def lighter_grey():
        return 0x95a5a6

    def dark_grey():
        return 0x607d8b

    def darker_grey():
        return 0x546e7a

    def og_blurple():
        return 0x7289da

    def blurple():
        return 0x5865F2

    def blurple():
        return 0x5865F2

    def greyple():
        return 0x99aab5

    def dark_theme():
        return 0x36393F

    def fuchsia():
        return 0xEB459E

    def yellow():
        return 0xFEE75C

    def green():
        return 0x2ecc71

    def blue():
        return 0x3498db

    def dark_blue():
        return 0x206694
    
    def purple():
        return 0x9b59b6

    def gold():
        return 0xf1c40f

    def dark_gold():
        return 0xc27c0e

    def orange():
        return 0xe67e22

    def dark_orange():
        return 0xa84300

    def brand_red():
        return 0xED4245