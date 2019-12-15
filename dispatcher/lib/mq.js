let amqp = require('amqplib');
let Log  = require('../lib/logger');

class MessageQueue {
    constructor() {
        this.host = 'localhost';
        this.queues = {};
        this.conn = null;
        this.channel = null;
    }

    static getQueue = async (queue) => {
        if (!MessageQueue.instance) {
            MessageQueue.instance = new MessageQueue();
        }

        let mq = MessageQueue.instance;
        if (!mq.queues[queue]) {
            mq.queues[queue] = await mq.connection(mq.host, queue);
        }

        return mq.queues[queue];
    };

    static sendMessage = async (queue, message) => {
        let mq = await MessageQueue.getQueue(queue);
        mq.sendToQueue(queue, Buffer.from(message));
    };

    connect = (host) => {
        Log.warning('Attempting to connect to message broker...');
        return new Promise((resolve, reject) => {
            amqp.connect('amqp://' + host)
                .then(conn => resolve(conn))
                .catch(err => reject(err))
        })
    };

    createChannel = (conn) => {
        return new Promise((resolve, reject) => {
            conn.createChannel()
                .then(channel => resolve(channel))
                .catch(err => reject(err))
        })
    };

    channelAssertQueue = (channel, queueName) => {
        return new Promise((resolve, reject) => {
            channel.assertQueue(queueName)
                   .then(asserted => resolve(channel))
                   .catch(err => reject(err))
        })
    };

    sendToQueue = (channel, queueName, buffer) => {
        channel.sendToQueue(queueName, buffer)
    };

    connection = async (host, queue) => {
        this.conn = await this.connect(host);
        this.conn.on("error", (error) => {
            if (error.message !== 'Connection closing') {
                this.queues = {};
                throw new Error('Error connecting to message broker');
            }
        });

        this.conn.on("close", () => {
            this.queues = {};
            Log.warning('Connection to queue closed, reconnecting...');
            return setTimeout(connection(host, queue), 1000);
        });

        let channel = await this.createChannel(this.conn);
        let assertedChannelToQueue = await this.channelAssertQueue(channel, queue);

        return channel;
    }

    // TODO: close method to handle interrupt(s) gracefully
}

module.exports = MessageQueue;
