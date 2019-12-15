let Log       = require('../lib/logger');
let MQ        = require('../lib/mq');
let JobModel  = require('../models/job');
let Validator = require('../lib/validator').JobDispatchRequestValidator;

class JobDispatcherController {
    constructor(request) {
        console.log(request.body);
        new Validator(request.body).validate();
        this.payload = request.body;
    }

    dispatch = async () => {
        let queueName    = 'image-processing';
        let queueMessage = new JobModel(this.payload).getQueueMessage();

        await MQ.sendMessage(queueName, queueMessage);

        Log.debug('Successfully added job to queue');

        return {status: 'enqueued', message: 'Successfully queued the job!'};
    };
}

module.exports = JobDispatcherController;
