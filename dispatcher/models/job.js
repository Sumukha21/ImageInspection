class Job {
    constructor(payload) {
        this.payload = payload;
    }

    getQueueMessage = () => {
        return JSON.stringify(this.payload);
    }
}

module.exports = Job;
