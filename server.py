const {Telegraf} = require ('telegraf')
const token ='6794189393:AAFRPg4nlC29DkgUGkpok2di7JujPyKGyCo'
const bot = new Telegraf(token);

bot.start((ctx) => ctx.reply("Hola"));

bot.launch();