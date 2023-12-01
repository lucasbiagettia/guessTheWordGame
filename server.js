import { Telegraf } from 'telegraf';
import { getSimilarity } from './similarityGetter.js';

const token = '6794189393:AAFRPg4nlC29DkgUGkpok2di7JujPyKGyCo';
const bot = new Telegraf(token);

bot.start((ctx) => ctx.reply("Hola"));

// Manejar cualquier mensaje de texto
bot.on('text', (ctx) => {
    // Obtener el texto del mensaje
    const texto = ctx.message.text;

    const response = getSimilarity(texto);

    // Hacer algo con el texto recibido
    ctx.reply(`Mensaje recibido: ${texto}, score: ${response}`);
});

bot.launch();
