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
