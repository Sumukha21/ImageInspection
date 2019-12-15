from lib.mq import MessageQueue
from app.processor import Processor
import logging

logger = logging.getLogger(__name__)


class Worker:
    def __init__(self, id):
        self.id = id

    def do_work(self):
        pass

class ImageProcessingWorker(Worker):
    def __init__(self, id):
        super().__init__(id)

    def do_work(self):
        def queue_consumer_callback(channel, method, properties, body):
            Processor(body).process_image_processing_payload()
            MessageQueue.get_instance().acknowledge('image-processing', method.delivery_tag)

        MessageQueue.get_instance().start_consuming('image-processing', queue_consumer_callback)
