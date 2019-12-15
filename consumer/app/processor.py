import json
import base64
import logging
import models.feature_extractor_main as FEMain

logger = logging.getLogger(__name__)


class Processor:
    def __init__(self, mq_message):
        payload = json.loads(mq_message)
        self.feature_extractor = payload.get('feature_extractor', {})
        self.img_bin = base64.b64decode(payload.get('img_bin', ''))

    def process_image_processing_payload(self):
        logger.info(json.dumps(self.feature_extractor))
        FEMain.staticMain(self.img_bin, feature_extractor_params=self.feature_extractor)
