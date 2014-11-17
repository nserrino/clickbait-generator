var http = require('http');
var xml2js = require('xml2js');

var sections = ['animals','celeb','tvandmovies','food','lgbt','music','politics','rewind','sports','lol','win','omg','cute','geeky','trashy','fail','wtf','books','breaking','comics','community','diy','ideas','longform','tech','travel','quiz','world','health'];

function getTitlesForNextSection() {
  var section = sections[0];

  http.get('http://www.buzzfeed.com/' + section + '.xml', function(res) {
    var buffers = [];

    console.log('## ' + section);

    res.on('data', function(chunk) {
      buffers.push(chunk);
    });
    res.on('end', function() {
      var buffer = Buffer.concat(buffers);
      var rssXml = buffer.toString();

      xml2js.parseString(rssXml, function(err, data) {
        if (err) {
          console.log('error parsing RSS XML: ' + err.message);
        } else {
          var items = data.rss.channel[0].item;
          items.map(function(item) {
            return item.title.toString();
          }).filter(function(title) {
            var firstToken = title.split(' ')[0];
            var number = parseInt(firstToken, 10);
            return !isNaN(number);
          }).forEach(function(title) {
            console.log(title);
          });
        }

        sections = sections.slice(1);
        if (sections.length) {
          console.log('');
          setTimeout(getTitlesForNextSection, 1000);
        }
      });
    });
  }).on('error', function(err) {
    console.log('problem with request: ' + err.message);
  });
}

getTitlesForNextSection();
