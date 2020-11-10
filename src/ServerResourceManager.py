#object pool
class Resource:
    """ Resources that clinet may use
    """
    __value = 0

    def reset(self):
        pass

    def setValue(self, number):
        pass

    def getValue(self):
        pass


class ServerObjectPool:
    """ Resource manager for clients requests.
    """

    __instance = None
    __resources = list()

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        pass

    def getResource(self):
        pass

    def returnResource(self, resource):
        pass
