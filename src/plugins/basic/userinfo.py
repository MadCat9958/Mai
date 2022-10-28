import lightbulb
import hikari

from config import setting
from utils import local, db

import datetime


plugin = lightbulb.Plugin("userinfo", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.option(
    "member", 
    "Укажите пользователя или ID для получения информации",
    type = hikari.OptionType.USER,
    required=False
)
@lightbulb.command(
    "userinfo", 
    "Показать информацию об пользователе"
)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: lightbulb.Context) -> None:
    
    if ctx.options.member is None:
        member = ctx.member
    else:
        member = ctx.options.member
    
    info = db.user(member.id)
    dtc = member.created_at.strftime('%Y-%m-%d %H:%M:%S')
    conv = datetime.datetime.strptime(dtc, '%Y-%m-%d %H:%M:%S').timestamp()

    l = local.localization(ctx.get_guild().id)

    emb = hikari.Embed(
            title=l["userinfo.title"],
            color = setting.color
        )
    emb.add_field(name = l["userinfo.user"], value=f"{member} | {member.id}")
    emb.add_field(name = l["userinfo.date"], value=f"<t:{round(conv)}:D> (<t:{round(conv)}:R>)")
    
    if not info:
        ...
    else:
        if info["profile"]["badge"] is not None:
            emb.add_field(name = l["userinfo.badge"], value = info["profile"]["badge"])
        if info["profile"]["bio"] is not None:
            emb.add_field(name = l["userinfo.bio"], value = info["profile"]["bio"])
        if info["blacklist"]["block"] == 1:
            emb.add_field(name = l["userinfo.block"], value = l["userinfo.block.reason"].format(info["blacklist"]["reason"]))
    
    emb.set_image(member.avatar_url)

    await ctx.respond(embed = emb)


def load(client):
    client.add_plugin(plugin)
