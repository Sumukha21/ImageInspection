from app.jobmanager import JobManager
import logging
import sys
import argparse

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--job', help='Name of the job to be performed by the worker', required=True)
    parser.add_argument('-w', '--workers', help='Number of workers to spawn to process jobs', required=True)

    args = parser.parse_args()
    JobManager().start_processing(args.job, worker_count=int(args.workers))
