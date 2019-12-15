import pika
import logging
import time
import os

logger = logging.getLogger(__name__)


class MessageQueue(object):
    instance = None

    def __init__(self):
        self.host = 'localhost'
        self.queues = {}
        self.connection = None
        self.create_connection()

    def create_connection(self):
        logger.info('Creating connection to message broker')
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        except Exception:
            logger.critical('Cannot connect to message broker, retrying in a while')
            time.sleep(10)
            self.create_connection()

    def create_channel(self, queue_name):
        if not self.connection or not self.connection.is_open:
            self.create_connection()

        channel = self.connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)

        return channel

    def start_consuming(self, queue_name, callback):
        channel = self.create_channel(queue_name)
        self.queues[queue_name] = channel
        channel.basic_consume(queue_name, callback, auto_ack=False)
        logger.info('Starting to consume from {} in process {}'.format(queue_name, str(os.getpid())))
        channel.start_consuming()

    @staticmethod
    def acknowledge(queue_name, delivery_tag):
        channel = MessageQueue.get_queue(queue_name)
        channel.basic_ack(delivery_tag)
        logger.info('Acknowledged consumption of a message')

    @staticmethod
    def get_instance():
        if MessageQueue.instance is None:
            MessageQueue.instance = MessageQueue()

        return MessageQueue.instance

    @staticmethod
    def get_queue(queue_name):
        mq = MessageQueue.get_instance()
        queue = mq.queues.get(queue_name, None)
        if queue is None:
            mq.create_channel(queue_name)

        return mq.queues[queue_name]
