var POP3Client = require("poplib");

port = 995;
host = "pop.gmail.com";
user = "test@newsie.club";
pass = "mypassword1";

var client = new POP3Client(port, host, {
    tlserrs: false,
    enabletls: true,
    debug: false
});

client.on("error", function(err) {

        if (err.errno === 111) console.log("Unable to connect to server");
        else console.log("Server error occurred");

        console.log(err);

});

client.on("connect", function() {

        console.log("CONNECT success");
        client.login(user, pass);

});

client.on("invalid-state", function(cmd) {
        console.log("Invalid state. You tried calling " + cmd);
});

client.on("locked", function(cmd) {
        console.log("Current command has not finished yet. You tried calling " + cmd);
});