from openwrt import services, users
from openwrt.core import Shell, RPCProxy
import portforwarding


class Manager:
    """
    A manager of a remote OpenWRT instance that provides more sophisticated management functionality that is not
    provided by the RPC interface directly.
    """

    def __init__(self, hostname, username, password):

        # Core modules
        self._rpc = RPCProxy(hostname, username, password)
        self._shell = Shell(self._rpc)

        # Managers
        self._services = services.ServicesManager(self._shell)
        self._portforwarding_manager = portforwarding.PortForwardingManager(self._rpc, self._services)
        self._users = users.UserManager(self._shell, self._rpc)

    @property
    def port_forwarding(self):
        return self._portforwarding_manager

    @property
    def services(self):
        return self._services

    @property
    def users(self):
        return self._users