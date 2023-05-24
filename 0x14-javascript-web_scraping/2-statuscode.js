#!/usr/bin/node
// This is script that display the status code of a GET request

const args = process.argv;
let request = require('request');
request(args[2], function (error, response, body) {
	if (error) {
		console.log('error:', error); // Print the error if it occurrs
		} else console.log('code:', response && response.statusCode);
});
