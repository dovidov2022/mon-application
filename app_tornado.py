import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    print("Starting Tornado server on http://0.0.0.0:8000")
    app = make_app()
    app.listen(8000, address="0.0.0.0")  # Changer ici pour 0.0.0.0
    tornado.ioloop.IOLoop.current().start()
