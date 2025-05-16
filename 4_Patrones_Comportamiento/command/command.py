from editor import EditorTexto
from comandosConcretos import AgregarTexto, BorrarTexto
from admin import AdministradorComandos

editor=EditorTexto()
admin=AdministradorComandos()
cmd1 = AgregarTexto(editor, "Tengo ")
admin.ejecutar(cmd1)
cmd2 = AgregarTexto(editor, "sueño, mucho.")
admin.ejecutar(cmd2)
editor.mostrar()
admin.deshacer()
editor.mostrar()
admin.rehacer()
editor.mostrar()
cmd3 = BorrarTexto(editor, 8)
admin.ejecutar(cmd3)
editor.mostrar()
admin.deshacer()
editor.mostrar()
