#/usr/bin/node
const files = require('fs');
files.writeFile(process.agrv[2],process.agrv[3],error => {
	if(error)console.log(error);
});
