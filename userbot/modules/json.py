# yaml_format is ported from uniborg
import io

from userbot.format import yaml_format, parse_pre
from userbot import MAX_MESSAGE_SIZE_LIMIT, CMD_HELP
from userbot.events import register

MAX_MESSAGE_SIZE_LIMIT = MAX_MESSAGE_SIZE_LIMIT


@register(outgoing=True, pattern=r"^.json(?: |$)([\s\S]*)")
async def _(event):
    if event.fwd_from:
        return
    the_real_message = None
    reply_id = pstl.reply_to_msg_id
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        catevent = await event.get_reply_message()
    the_real_message = catevent.stringify()
    if len(the_real_message) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "json.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await edit_or_reply(event, the_real_message, parse_mode=parse_pre)


@register(outgoing=True, pattern=r"^.yaml(?: |$)([\s\S]*)")
async def _(event):
    if event.fwd_from:
        return
    the_real_message = None
    reply_id = pstl.reply_to_msg_id
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        catevent = await event.get_reply_message()
    the_real_message = yaml_format(catevent)
    if len(the_real_message) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "yaml.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await edit_or_reply(event, the_real_message, parse_mode=parse_pre)


CMD_HELP.update(
    {
        "json": """**Plugin : **`json`

  •  **Syntax : **`.json reply`
  •  **Function : **__reply to a message to get details of that message in json format__  

  •  **Syntax : **`.yaml reply`
  •  **Function : **__reply to a message to get details of that message in yaml format__ """
    }
)
