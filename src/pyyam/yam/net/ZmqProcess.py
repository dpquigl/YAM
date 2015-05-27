# coding=utf-8>

import multiprocessing

from yam.datatype.Enum import Enum
from zmq.eventloop import ioloop, zmqstream
import zmq
from collections import namedtuple

def strToTransportType(trans):
    if trans is "tcp":
        return TransportTypes.tcp
    elif trans is "inproc":
        return TransportTypes.inproc
    elif trans is "ipc":
        return TransportTypes.ipc
    else:
        return TransportTypes.none
    
TransportTypes = Enum(["none", "tcp","inproc","ipc"])    

Address = namedtuple('Address', ['type', 'host', 'port', 'resource'])

class ZmqProcess(multiprocessing.Process):
    """
    This is the base for all processes and offers utility functions
    for setup and creating new streams.

    """
    def __init__(self):
        super(ZmqProcess, self).__init__()

        self.context = None
        """The ØMQ :class:`~zmq.Context` instance."""

        self.loop = None
        """PyZMQ's event loop (:class:`~zmq.eventloop.ioloop.IOLoop`)."""

    def setup(self):
        """
        Creates a :attr:`context` and an event :attr:`loop` for the process.

        """
        self.context = zmq.Context()
        self.loop = ioloop.IOLoop.instance()

    def stream(self, sock_type, addr, bind, callback=None, subscribe=b''):
        """
        Creates a :class:`~zmq.eventloop.zmqstream.ZMQStream`.

        :param sock_type: The ØMQ socket type (e.g. ``zmq.REQ``)
        :param addr: Address to bind or connect to in the formed of an Address named tuple
                
                For the tcp transport type *(host, port)* or *host* (bind to random port).
                If *bind* is ``True``, *host* may be:

                - the wild-card ``*``, meaning all available interfaces,
                - the primary IPv4 address assigned to the interface, in its
                numeric representation or
                - the interface name as defined by the operating system.

                If *bind* is ``False``, *host* may be:

                - the DNS name of the peer or
                - the IPv4 address of the peer, in its numeric representation.

                If *addr* is just a host name without a port and *bind* is
                ``True``, the socket will be bound to a random port.
                
                For the inproc and ipc transport types the address must contain a resource
        :param bind: Binds to *addr* if ``True`` or tries to connect to it
                otherwise.
        :param callback: A callback for
                :meth:`~zmq.eventloop.zmqstream.ZMQStream.on_recv`, optional
        :param subscribe: Subscription pattern for *SUB* sockets, optional,
                defaults to ``b''``.
        :returns: A tuple containg the stream and the port number.

        """
        sock = self.context.socket(sock_type)

        # Bind/connect the socket
        if bind:
            if addr.type is TransportTypes.tcp:
                if addr.port:
                    sock.bind('tcp://%s:%s' % (addr.host, addr.port))
                else:
                    addr.port = sock.bind_to_random_port('tcp://%s' % addr.host)
            elif addr.type is TransportTypes.inproc or addr.type is TransportTypes.ipc:
                address = "%s://%s" % (addr.type,addr.resource)
                sock.bind(address)
        else:
            if addr.type is TransportTypes.tcp:
                address = "tcp://%s:%s" % (addr.host, addr.port)
            elif addr.type is TransportTypes.inproc or addr.type is TransportTypes.ipc:
                address = "%s://%s" % (addr.type,addr.resource)
            sock.connect(address)
        # Add a default subscription for SUB sockets
        if sock_type == zmq.SUB:
            sock.setsockopt(zmq.SUBSCRIBE, subscribe)

        # Create the stream and add the callback
        stream = zmqstream.ZMQStream(sock, self.loop)
        if callback:
            stream.on_recv(callback)

        return stream
    
    def run(self):
        """Sets up everything and starts the event loop."""
        self.setup()
        self.loop.start()

    def stop(self):
        """Stops the event loop."""
        self.loop.stop()