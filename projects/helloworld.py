from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('Hello %(name)s!' % request.matchdict)

def show_kitten(request):
    return Response('<body><img alt="" src="http://res.freestockphotos.biz/pictures/9/9343-a-cute-orange-kitten-isolated-on-a-white-background-pv.jpg"></body>')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')
    config.add_route('kitten', '/')
    config.add_view(show_kitten, route_name='kitten')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
   
