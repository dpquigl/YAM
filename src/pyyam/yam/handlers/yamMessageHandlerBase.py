class yamMessageHandlerBase(object):
    """
    Base class for message handlers for a :class:`ZMQProcess`.

    Inheriting classes only need to implement a handler function for each
    message type. It must assign the protobuf Message class to self.cls and 
    create a mapping of message types to handler functions

    """
    def __init__(self, rep_stream, stop):
        self._rep_stream = rep_stream
        self._stop = stop
        self.cls = None
        self.funcMap = {}
        self.subMessageHandler = False
        pass
    
    def __call__(self, msg):
        """
        Gets called when a messages is received by the stream this handlers is
        registered at. *msg* is a list as return by
        :meth:`zmq.core.socket.Socket.recv_multipart`.

        """   
        
        
        if self.subMessageHandler:
            yamMessage = msg
        else:
            yamMessage = self.cls()
            fullMsg = "".join(msg)
            yamMessage.ParseFromString(fullMsg)

        handlerFunc = self.funcMap[yamMessage.type]
        responseMessage = handlerFunc(yamMessage)
        
        return responseMessage      
