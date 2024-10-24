class ConnectorFactory:

    CONNECTORS = {}

    @classmethod
    def register_connector(cls, identifier, cls_name):
        cls.CONNECTORS[identifier] = cls_name

    @classmethod
    def pick_connector(cls, identifier, protocol, attributes):
        pass
