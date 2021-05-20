from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club

#  Lectura de archivos txt de Club y Jugadores
clubs = open('data/datos_clubs.txt', 'r', encoding='utf-8')
jugadores = open('data/datos_jugadores.txt', 'r', encoding='utf-8')
    
# Ingreso de datos Clubs
for c in clubs:
    cadenaClub = c.split(";")
    cadenaClub[-1] = cadenaClub[-1].strip()
    session.add(Club(nombre=cadenaClub[0], deporte=cadenaClub[1], fundacion=cadenaClub[-1]))
  

# Ingreso de datos Jugadores             
consultaClub = session.query(Club).all()

for j in jugadores:
    cadenaJugadores = j.split(";")
    cadenaJugadores[-1] = cadenaJugadores[-1].strip()
    
    for club in consultaClub:
        if(cadenaJugadores[0] == club.nombre):
            id_club = club.id
            
    session.add(Jugador(nombre=cadenaJugadores[3], dorsal=cadenaJugadores[2], posicion=cadenaJugadores[1], club_id= id_club))
   
# se confirma las transacciones
session.commit()
