let express       = require('express');
let Response      = require('../views/response');
let Log           = require('../lib/logger');
let Errors        = require('../lib/errors');
let JobDispatcher = require('../controllers/dispatcher');
let router        = express.Router();

router.post('/', async (req, res, next) => {
    let response;
    try {
        const data = await new JobDispatcher(req).dispatch();
        response   = new Response.Success(data);
    } catch (e) {
        Log.critical('Failed to dispatch job', e);
        if (e instanceof Errors.ValidationError) {
            response = new Response.ValidationError(e);
        } else {
            response = new Response.ServerError();
        }
    }

    response = response.render();
    res.status(response.error_code).json(response.data);
});

module.exports = router;
