from handlers.foo import FooHandler
from handlers.home import HomeIndexHandler

url_patterns = [
    (r"/foo", FooHandler),
    (r"/", HomeIndexHandler),
]
