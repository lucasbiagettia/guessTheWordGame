import axios from 'axios';

async function convertirADouble(string) {
  try {
    const response = await axios.post('http://localhost:8000/convertirADouble', {
      string
    });

    const resultado = response.data.resultado;
    console.log(response.data)
    return resultado;
  } catch (error) {
    console.error('Error al convertir el string a double:', error);
    throw error;
  }
}

// Función async para manejar la asincronía
async function ejecutarConversion() {
  try {
    const resultado = await convertirADouble('I like pizza');
    console.log(`Resultado: ${resultado}`);
  } catch (error) {
    console.error('Error durante la conversión:', error);
  }
}

// Llamar a la función async
(async () => {
  try {
    await ejecutarConversion();
    // Hacer algo después de que se complete la conversión
  } catch (error) {
    console.error('Error en la cadena de promesas:', error);
  }
})();
