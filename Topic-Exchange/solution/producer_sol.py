
from producer_interface import mqProducerInterface


class mqProducer(mqProducerInterface):

    def __init__(self, routing_key: str, exchange_name: str) -> None:
        mqProducerInterface.__init__(self,routing_key,exchange_name)

    
    def publishOrder(self, message: str) -> None:
        return super().publishOrder(message)

        
