# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import pika,sys
class mqProducerInterface:
    def __init__(self, exchange_name: str) -> None:
        routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
        self.routing_key = routing_key
        # Save parameters to class variables
        self.exchange_name = exchange_name
        self.ticker = sys.argv[2]
        self.price = sys.argv[3]
        self.sector = sys.argv[4]

        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(rouuting_key = self.routing_key,exchange=self.exchange_name,exchange_type = "topic")

    def publishOrder(self, message: str) -> None:
        # Create Appropiate Topic String

        # Send serialized message or String

        # Print Confirmation

        # Close channel and connection

        pass
