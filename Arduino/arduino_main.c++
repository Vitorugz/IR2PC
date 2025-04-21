#include <IRremote.h>

const int recvPin = 8; // Pino 8 onde o receptor IR está conectado

IRrecv irrecv(recvPin); // Objeto para receber sinais IR
decode_results results; // Objeto para armazenar os resultados recebidos

void setup()
{
    Serial.begin(9600);  // Inicializa a comunicação serial
    irrecv.enableIRIn(); // Inicia o receptor IR
}

void loop()
{
    // Verifica se algum sinal IR foi recebido
    if (irrecv.decode(&results))
    {
        long int decCode = results.value; // Obtém o código IR recebido

        // Exibe o código recebido no Monitor Serial
        Serial.println(decCode, HEX); // Exibe o código em formato hexadecimal
        delay(150);

        irrecv.resume(); // Prepara o receptor para a próxima leitura
    }
}
