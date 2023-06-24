var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("mydb");
  var myquery = { address: /^H/ };
  dbo.collection("customers").deleteMany(myquery, function(err, res) {
    if (err) throw err;
    console.log(res.deletedCount + " document(s) deleted");
    db.close();
  });
}); 