let express      = require('express');
let path         = require('path');
let cookieParser = require('cookie-parser');
let logger       = require('morgan');
let cors         = require('cors');

let defaultRouter    = require('./routes/default');
let dispatcherRouter = require('./routes/dispatcher');

let app = express();

app.use(logger('dev'));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
// TODO: add a request deduplication middleware

app.use('/', defaultRouter);
app.use('/dispatch', dispatcherRouter);

module.exports = app;
