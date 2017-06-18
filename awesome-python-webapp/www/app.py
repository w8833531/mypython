#!/usr/bin/env python
# coding=utf8
#由于我们的Web App建立在asyncio的基础上，因此用aiohttp写一个基本的app.py
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from aiohttp import web
def index(request):
    return web.Response(body=b'<h1> Awesome </h1>', content_type='text/html')

async def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '0.0.0.0', 5000)
    logging.info('server started at http://139.224.113.226:5000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

