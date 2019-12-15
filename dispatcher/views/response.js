class Response {
    constructor(errorCode, data) {
        this.errorCode  = errorCode;
        this.data       = data;
    };

    render = () => ({
        error_code: this.errorCode,
        data      : this.data
    });
}

class ServerError extends Response {
    constructor() {
        super(500, {message: 'Something went wrong! (Internal Error)'});
    }
}

class ValidationError extends Response {
    constructor() {
        super(400, {message: 'Bad request! Failed to validate payload'});
    }
}

class Success extends Response {
    constructor(data) {
        super(200, data);
    }
}

module.exports = {
    ServerError    : ServerError,
    ValidationError: ValidationError,
    Success        : Success
};
