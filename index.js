const Discord = require('discord.js');
const client = new Discord.Client();

var counter = 0;

client.on('message', message => {

  if (message.author.id == "339609439143460867"){
    message.author.send("SHUT THE FUCK UP");
  }

});



client.login(process.env.SNAKER_TOKEN);
