from app.jobmanager import JobManager
import logging
import sys


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    JobManager().start_processing('image-processing', worker_count=2)
