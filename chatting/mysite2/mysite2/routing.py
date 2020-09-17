from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat2.routing

application = ProtocolTypeRouter({
    #(http->django views is added by default)
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            chat2.routing.websocket_urlpatterns
        )
    ) 
})