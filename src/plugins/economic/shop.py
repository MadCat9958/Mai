import lightbulb
import hikari
import miru

from config import setting
from utils import local, access, db

plugin = lightbulb.Plugin("shop", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(access.disable_command)
@lightbulb.option(
    name="list",
    description="Выберите из списка, что вы хотите купить",
    type = hikari.OptionType.STRING,
    choices=[
        "Удочка",
        "Крючок",
        "Баннер"
    ],
    required=False
)
@lightbulb.option(
    name="id",
    description="ID покупки",
    type= hikari.OptionType.INTEGER,
    required=False
)
@lightbulb.command("shop", "Глобальный магазин бота")
@lightbulb.implements(lightbulb.SlashCommand)
async def shop(ctx: lightbulb.Context) -> None:
    l = local.localization(ctx.get_guild().id)
    user = db.user(ctx.author.id)
    list = ctx.options.list

    class ShopButton(miru.View):

        @miru.button(emoji="🎣", style=hikari.ButtonStyle.SECONDARY)
        async def rod_list(self, button: miru.Button, ctx: miru.ViewContext) -> None:
            emb = (
                hikari.Embed(
                    title="Список доступных удочек",
                    description="ID:1 **Палочка с веревкой** 100 :coin:",
                    color=setting.color
                )
            )
            await ctx.respond(
                embed=emb,
                component=None,
                flags=hikari.MessageFlag.EPHEMERAL
            )

        @miru.button(emoji="🪝", style=hikari.ButtonStyle.SECONDARY)
        async def fish_hook_list(self, button: miru.Button, ctx: miru.ViewContext) -> None:
            emb = (
                hikari.Embed(
                    title="Список доступных крючков",
                    description="ID:1 **Червяк** 250:coin:",
                    color=setting.color
                )
            )
            await ctx.respond(
                embed=emb,
                component=None,
                flags=hikari.MessageFlag.EPHEMERAL
            )

        @miru.button(emoji="🖼️", style=hikari.ButtonStyle.SECONDARY)
        async def banner_list(self, button: miru.Button, ctx: miru.ViewContext):
            emb = (
                hikari.Embed(
                    title="Список доступных баннеров",
                    description="Весь список баннеров находиться [здесь](https://boticord.gay)",
                    color=setting.color
                )
            )
            await ctx.respond(
                embed=emb,
                component=None,
                flags=hikari.MessageFlag.EPHEMERAL
            )


    emb = (
        hikari.Embed(
            title="Магазин бота",
            description="Здесь вы можете покупать как удочки и крючки, так и баннеры для своего профиля\nДля дополнительной информацией посетите [документацию](https://docs.maibot.xyz)",
            color=setting.color
        )
    )

    if list or ctx.options.id == None:
        button = ShopButton()
        msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
        await button.start(msg)
        return

    if list == "Удочка":
        id = int(ctx.options.id)

        if user["rod"] >= id:
            await ctx.respond("У вас уже есть такая удочка или была в использовании")
            return

        if id <= 0:
            await ctx.respond(123)
            return

        if id == 1:
            if user["coin"] < 900:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 2:
            if user["coin"] <= 2000:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 3:
            if user["coin"] <= 4500:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 4:
            if user["coin"] <= 7800:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 5:
            if user["coin"] <= 11000:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 6:
            if user["coin"] <= 16500:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 7:
            if user["coin"] <= 20000:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 8:
            if user["coin"] <= 27000:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 9:
            if user["coin"] <= 40000:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        else:
            await ctx.respond("такой удочки не существует")

    if list == "Крючок":
        id = int(ctx.options.id)

        if user["fish_hook"] >= id:
            await ctx.respond("У вас уже есть такой крючок или был в использовании")
            return

        if id <= 0:
            await ctx.respond(123)
            return

        if id == 1:
            if user["coin"] <= 250:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 2:
            if user["coin"] <= 500:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 3:
            if user["coin"] <= 1250:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 4:
            if user["coin"] <= 2500:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 5:
            if user["coin"] <= 3600:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        if id == 6:
            if user["macoin"] <= 25:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        else:
            await ctx.respond("такого крючка не существует")

def load(client):
    client.add_plugin(plugin)