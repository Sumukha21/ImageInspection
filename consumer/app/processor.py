import json
import base64
import logging

logger = logging.getLogger(__name__)


class Processor:
    def __init__(self, mq_message):
        payload = json.loads(mq_message)
        self.feature_extractor = payload.get('feature_extractor', {})
        self.img_bin = base64.b64decode(payload.get('img_bin', ''))

    def process_image_processing_payload(self):
        logger.info(json.dumps(self.feature_extractor))
        import os
        print(str(os.getpid()))
        print(self.img_bin)
