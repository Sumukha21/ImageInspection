import multiprocessing
import logging
import time
from app.worker import ImageProcessingWorker

logger = logging.getLogger(__name__)


class JobManager:
    def __init__(self):
        self.num_cores = multiprocessing.cpu_count()
        self.job_worker_map = {
            'image-processing': ImageProcessingWorker
        }
        self.job_workers = []

    def start_processing(self, job, worker_count=1):
        if worker_count > self.num_cores:
            logger.warning('Worker count given ({}) is more than the number of available cores, continuing with worker count '
                           'equal to the number of available cores ({})'.format(worker_count, self.num_cores))

        worker_class = self.job_worker_map.get(job)
        if not worker_class:
            raise Exception('Worker class for {} not found'.format(job))

        for i in range(worker_count):
            def target_function():
                try:
                    worker_class(job + '-' + str(i)).do_work()
                except Exception as e:
                    raise e
                    logger.critical('Worker {} encountered exception {}'.format(job, str(e)))
                    time.sleep(3)
                    target_function()

            worker_process = multiprocessing.Process(target=target_function)
            worker_process.start()
            self.job_workers.append(worker_process)

        for worker in self.job_workers:
            worker.join()

    # TODO: add stop_processing() and handle interrupt(s) gracefully
