from formulario import Formulario
from validadores import ValidarCamposVacios, ValidarFormatoCorreo, ValidarDuplicado

formulario = Formulario("Steven", "steven@gmail.com")
datos = formulario.obtener_datos()

validador_vacio = ValidarCamposVacios()
validador_formato = ValidarFormatoCorreo()
validador_duplicado = ValidarDuplicado()

validador_vacio.enlazar(validador_formato).enlazar(validador_duplicado)

if validador_vacio.manejar(datos):
    print("Formulario enviado éxitosamente.")
else:
    print("Formulario inválido. Corrige los errores en la información o rellena los campos correspondientes.")
