"""Controls the interaction with Discord using the interactions module."""

import os
from interactions import (SlashContext, OptionType, Client, listen,
                          SlashCommand, slash_option)
import traceback
from interactions.api.events import CommandError

import Fail_functions
from Fail_functions import send_random_img_url
import json
from Fail_functions import add_fail ,add_praise, count_score

@listen()
async def on_ready():
    """Lets the console know when the bot is online."""
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


# @listen(CommandError, disable_default_listeners=True)  # tell the dispatcher that this replaces the default listener
# async def on_command_error(event: CommandError):
#     """Listens for any errors in slash commands. If an error is raised, this listener will catch it and store all the
#     error messages in event.error. These errors are sent to the person who used the slash command as an ephemeral msg.
#
#     :param event: (object) contains information about the interaction
#     """
#     traceback.print_exception(event.error)
#     if not event.ctx.responded:
#         errors = ''
#         if event.error.args[0]:
#             errors = '\nAlso! '.join(event.error.args)
#         await event.ctx.send('Error! ' + errors, ephemeral=True)


# Base command
base_command = SlashCommand(
    name="fail",
    description="Someone's been naughty. Time to fetch the paddle",
    scopes=[1193614893870489720])


@base_command.subcommand(sub_cmd_name="punish",
                         sub_cmd_description="say fail in the nicest way possible")
async def award_points(ctx: SlashContext):
    """Just says hi... for now ;)

    :param ctx: (object) contains information about the interaction
    """
    Fail_functions.add_fail()
    images = Fail_functions.send_random_img_url('gelbooru_img_urls.json')
    # Send 'hi' to Discord
    await ctx.send(images)

@base_command.subcommand(sub_cmd_name="praise",
                         sub_cmd_description="gives praise!")
async def award_points2(ctx: SlashContext):

    Fail_functions.add_praise()
    images = Fail_functions.send_random_img_url('gelbooru_img_urls.json')
    await ctx.send(images)


@base_command.subcommand(sub_cmd_name="score",
                         sub_cmd_description="keeps track of praise and punishments")
async def count_score(ctx: SlashContext):
    score = Fail_functions.count_score()
    await ctx.send(print(score))

if __name__ == "__main__":
    # Set the cwd to the directory where this file lives
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Define and start the bot
    var1 = "MTIwNzk2MTE5NzkwMzc0NTAyNA.GMEIn-"
    var2 = ".NBDrwWCO16SYnyzE0IEwQkjngAi746pgPRBNKA"
    bot_token = var1 + var2
    bot = Client(token=bot_token)
    bot.start()
