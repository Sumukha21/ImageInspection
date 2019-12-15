let express = require('express');
let router = express.Router();

/* GET default page. */
router.get('/', function(req, res, next) {
  res.status(404).render('default', { title: 'Dispatcher 404' });
});

module.exports = router;
