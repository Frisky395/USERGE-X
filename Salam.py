# All rights reserved.

import asyncio
import os
import time
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub

import requests
import wget
from cowpy import cow

from userge import Message, userge


@userge.on_cmd("p$", about={"header": "Memberi salam"})
async def p_(message: Message):
    """Salam"""
    await check_and_send(message, "`Assalamualaikum`")


@userge.on_cmd("l$", about={"header": "Memberi salam"})
async def l_(message: Message):
    """Salam"""
    await check_and_send(message, "`Wa'alaikumussalam`")
