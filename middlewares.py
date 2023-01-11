from __future__ import annotations

from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery, InlineQuery, Message, ChatJoinRequest

from users import get_or_create_user


class UsersMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict[str]):
        if "channel_post" in message or message.chat.type != "private":
            raise CancelHandler()

        user = message.from_user

        data["user"] = get_or_create_user(
            user.id, user.username
        )

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        user = callback_query.from_user

        data["user"] = get_or_create_user(
            user.id, user.username
        )

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        user = inline_query.from_user

        data["user"] = get_or_create_user(
            user.id, user.username
        )

    @staticmethod
    async def on_process_chat_join_request(chat_member: ChatJoinRequest, data: dict[str]):
        user = chat_member.from_user

        data["user"] = get_or_create_user(
            user.id, user.username
        )

    
