let Joi    = require('joi');
let Errors = require('./errors');
let Log    = require('./logger');

class Validator {
    constructor(payload) {
        this.schema  = {
            client_ts: Joi.string(),
            request_id: Joi.string().required()
        };
        this.payload = payload;
    }

    validate = () => {
        let result = Joi.validate(this.payload, this.schema, {allowUnknown: true});
        if (result.error) {
            throw new Errors.ValidationError(result.error);
        }
    }
}

class JobDispatchRequestValidator extends Validator {
    constructor(payload) {
        super(payload);
        this.schema.img_bin = Joi.string().required();
        this.schema.feature_extractor = Joi.object().required();

    }
}

module.exports = {
    JobDispatchRequestValidator: JobDispatchRequestValidator
};
