# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def telegram_start(self, turn_context: TurnContext):
        if turn_context.activity.text == "/start":
            await turn_context.send_activity(f"Hi from SupplyBot on Telegram! You can let me know which stores have disinfectant, masks or toiletpaper. I'll let you're local Covid-crisis response volunteer groups know so they can deliver them to at risk people")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hi from SupplyBot! You can let me know which stores have disinfectant, masks or toiletpaper. I'll let you're local Covid-crisis response volunteer groups know so they can deliver them to at risk people")
