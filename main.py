import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} er online.")

@bot.command()
async def setup_fragzone(ctx):
    guild = ctx.guild
    await ctx.send("⚙️ Dansk FragZone bliver sat op...")

    # Roller
    roles = ["Admin", "Medlem", "Premium", "18+", "21+", "25+", "CS2", "Valorant", "LoL", "CoD"]
    for role in roles:
        if not discord.utils.get(guild.roles, name=role):
            await guild.create_role(name=role)

    # Kategorier og kanaler
    categories = {
        "📌 INFO": ["📌start-her", "📜regler", "📣nyheder"],
        "🎮 SPIL & MATCH": ["🎯rang", "🎂alder-valg", "🤖bot-kommandoer", "🧠match-log"],
        "💬 FÆLLESSKAB": ["💬fællesskab"],
        "🎧 VOICE": [
            "🎤 Snakkehjørnet 1", "🎤 Snakkehjørnet 2", "🎤 TeamFlash 1", "🎤 TeamFlash 2",
            "🎤 TeamFlash 3", "🎤 TeamFlash 4", "🎤 TeamFlash 5", "🎤 TeamFlash 6",
            "🎤 Wingman / MM", "🎤 AFK"
        ],
        "🎮 GAME VOICE": [
            "🎤 CS2 Voice 1", "🎤 CS2 Voice 2", "🎤 Valorant Voice 1", "🎤 Valorant Voice 2",
            "🎤 LoL Voice 1", "🎤 LoL Voice 2", "🎤 COD Voice 1", "🎤 COD Voice 2"
        ],
        "📞 SUPPORT": ["📥support-ticket", "🎤 support voice"]
    }

    for cat_name, chans in categories.items():
        category = discord.utils.get(guild.categories, name=cat_name)
        if not category:
            category = await guild.create_category(cat_name)
        for chan in chans:
            if "🎤" in chan:
                if not discord.utils.get(guild.voice_channels, name=chan):
                    await guild.create_voice_channel(chan, category=category)
            else:
                if not discord.utils.get(guild.text_channels, name=chan):
                    await guild.create_text_channel(chan, category=category)

    await ctx.send("✅ Dansk FragZone er sat op og klar!")

bot.run(TOKEN)
