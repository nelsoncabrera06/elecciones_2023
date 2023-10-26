# elecciones_2023



Desde aca te podes descargar el crudo de los resultados
https://www.argentina.gob.ar/dine/resultados-electorales/elecciones-2023


hay un archivo .csv, ResultadosElectorales_2023.csv
1,2Gb pesa
en excel esto no se puede abrir, o no lo muestra completo al menos
tampoco estan todas las mesas escrutadas al 100%


Mi script lo que hace crea una copia con dos nuevas columnas total_votos_en_mesa y porcentaje, ejemplo:
224	42,41
215	38,14
219	42,01
231	35,5
236	40,25

Con estos valores despues es mas facil filtrar en lugar donde aparecen numeros raros.
No es perfecto, porque filtra por mesa, pero deberia ser un filtro mas grande, por provincia, municipio, distrito, comuna lo que sea, para no hacer errores con mesas que tienen el mismo numero.

Pero le idea general esta bien, faltaria hacer un filtro mas grande nomas.

Si crees que encontraste algo raro, podes ir a chequear esa mesa en:
https://resultados.gob.ar/


-----

Para correrlo solo es necesario tirar el sigiuente comando en el terminal "python3 check.py"

todo esto lo estuve probando con test_mis_resultados.csv
que es una copia ResultadosElectorales_2023.csv (el archivo original pesado)
pero con muchisimas menos lineas, mas liviano para poder probar cosas.
nunca lo probe con el archivo original ResultadosElectorales_2023.csv todavia
