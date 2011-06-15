#! /usr/bin/env python

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello from python, ' + name + '!'

if __name__ == "__main__":
    app.run()
