from logPrototype import Log
from logManager import GestorLogs

log_info=Log("Info", "Operación realizada éxitosamente.", "Sistema")
log_error=Log("Error", "Error.", "Base de datos")
log_debug=Log("Debug", "Valor de variable fuera de rango.", "Backend")

gestor=GestorLogs()
gestor.registrar("info", log_info)
gestor.registrar("error", log_error)
gestor.registrar("debug", log_debug)

log1=gestor.obtener("info")
log1.mensaje="Usuario creado correctamente."
log1.origen="Usuarios."

log2=gestor.obtener("error")
log2.mensaje="Error al conectar al server."
log2.origen="Red"

log3=gestor.obtener("debug")
log3.mensaje="Variable 'x' tiene valor None."
log3.origen="Controlador"

log1.mostrar()
log2.mostrar()
log3.mostrar()