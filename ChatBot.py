from ChatBotBrain import ChatBotBrain
from Api import Api
import re

class ChatBot:
    def __init__(self, context, seed, model, tokenizer, first_message):
        self.brain = ChatBotBrain(context, seed, model, tokenizer)
        self.first_message = first_message
        self.init_answers()
        self.api = Api()

    def run(self):
        while True:
            dictionary = self.api.update(self.api.last_message)
            for m in dictionary['result']:
                id_chat, user, question, id_update = self.api.read_messages(m)

                if id_update > (self.api.last_message-1):
                    self.api.last_message = id_update + 1

                if self.filter_question(question.lower(), id_chat):
                    self.api.send_message(id_chat, self.brain.talk(question))
                    # print('RoboTec dice >>', self.brain.talk(question))

    def filter_question(self, question, id_chat):
        for answer in self.answers:
            pattern = answer[0]
            p = re.compile(pattern)
            if not p.search(question.lower()) is None:
                self.api.send_message(id_chat, answer[1])
                # print('RoboTec dice >>', answer[1])
                return False
        return True
        

    def init_answers(self):
        self.answers = [
            (
                '(.*)telefono(.*)escuela(.*)',
                'Puedes contactarnos por el siguiente Numero: 3111421169'
            ),
            (
                '(.*)baños(.*)',
                'Puedes Ubicar los baños en los siguientes edificios: Baston, Laboratorio de computo, Centro de Idiomas, Biblioteca, Edificio X, Domo, LICBI, Edificio UD'
            ),
            (
                '(.*)(donde|ubicacion)(.*)baston(.*)',
                'El edificio baston se encuentra por la entrada peatonal principal, primer edificio de la izquierda. \n Aqui tienes la ubicacion:  https://goo.gl/maps/Xj2HTpdMqjXUYLiJ7 '
            ),
            (
                '(.*)(donde|ubicacion)(.*)ud(.*)',
                'El edificio UD se encuentra por la entrada peatonal principal, primer edificio de la derecha. \n Aqui tienes la ubicacion: https://goo.gl/maps/oxmE7phGNeYLMqbx7'
            ),
            (
                '(.*)(donde|ubicacion)(.*)licbi(.*)',
                'El edificio LICBI se encuentra por la entrada 2 de agosto, primer edificio de la izquierda. \n Aqui tienes la ubicacion: https://goo.gl/maps/uUw8EZ3fDpiBt5737'
            ),
            (
                '(.*)(donde|ubicacion)(.*)recursos(.*)',
                'El Departamento de Recursos Financieros se encuentra por la entrada principal, segundo edificio de la derecha. \n Aqui tienes la ubicacion: https://goo.gl/maps/JaWjrciqcj5mHa8S9'
            ),
            (
                '(.*)(donde|ubicacion)(.*)domo(.*)',
                'El Domo se encuentra entrando por la entrada principal, todo derecho pasando los edificios, y las canchas de futbol. \n Aqui tienes la ubicacion: https://goo.gl/maps/VUGRbTS4JFnbFwTA6'
            ),
            (
                '(.*)(donde|ubicacion)(.*)futbol(.*)',
                'La cancha de Futbol se encuentra entrando por la entrada principal, todo derecho, hasta donde topes, giras a la derecha y detras de los laboratorios de quimica. \n Aqui tienes la ubicacion: https://goo.gl/maps/BNQdxcGAMptjz6gC6'
            ),
            (
                '(.*)(donde|ubicacion)(.*)beisbol(.*)',
                'La cancha de Beisbol se encuentra entrando por la entrada principal, todo derecho pasando los edificios, a un costado del Domo. \n Aqui tienes la ubicacion: https://goo.gl/maps/5dhBQU49Zbisis1e8'
            ),
            (
                '(.*)(donde|ubicacion)(.*)basquetbol(.*)',
                'La cancha de Basquetbol se encuentra entrando por la entrada principal, todo derecho pasando los edificios, y las canchas de volibol. \n Aqui tienes la ubicacion: https://goo.gl/maps/XJ4jYRK99ghdR93T6'
            ),
            (
                '(.*)(donde|ubicacion)(.*)cafeteria(.*)',
                'La Cafeteria se encuentra frente a la entrada 2 de agosto, a un costado del estacionamiento. \n aqui tienes la ubicacion: https://goo.gl/maps/mS6jqNAG5u2zMbF57'
            ),
            (
                '(.*)(donde|ubicacion)(.*)biblioteca(.*)',
                'La biblioteca se encuentra por la entrada principal, todo derecho, terminando el pasillo a la derecha y es el edifico de al fondo. \n aqui tienes la ubicacion: https://goo.gl/maps/FMw6jWqBFHiy7hCo6'
            ),
            (
                '(.*)oferta educativa(.*)',
                'Puedes ver nuestras oferta educativa en el siguiente link: \nhttps://www.tepic.tecnm.mx/ofertaeducativa'
            ),
            (
                '(.*)facebook(.*) tepic(.*)',
                'Este es nuestro Facebook link: \nhttps://m.facebook.com/TecnologicodeTepic/'
            ),
            (
                '(.*)facebook(.*)sistemas(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/profile.php?id=100006319297206'
            ),
            (
                '(.*)facebook(.*)desarrollo(.*)',
                'Este es nuestro Facebook link: \nhttps://m.facebook.com/Desarrollo-Acad%C3%A9mico-Oferta-Educativa-ITT-106762494071023/'
            ),
            (
                '(.*)facebook(.*)arquitectura(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/coordinacion.arquitectura.tectepic'
            ),
            (
                '(.*)facebook(.*)movilidad(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/profile.php?id=100010331235200'
            ),
            (
                '(.*)facebook(.*)quimica(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/profile.php?id=100008518719760'
            ),
            (
                '(.*)facebook(.*)bioquimica(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/profile.php?id=100008518719760'
            ),
            (
                '(.*)facebook(.*)mecatronica(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/coordinacion.ie.im'
            ),
            (
                '(.*)facebook(.*)industrial(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/coordinacion.ingindustrial.3'
            ),
            (
                '(.*)facebook(.*)lenguajes(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/cle.ittepic'
            ),
            (
                '(.*)facebook(.*)administracion(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/profile.php?id=100011687321637'
            ),
            (
                '(.*)facebook(.*)civil(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/profile.php?id=100012151927234'
            ),
            (
                '(.*)facebook(.*)titulacion(.*)',
                'Este es nuestro Facebook link: \nhttps://www.facebook.com/laura.casillas.792303'
            ),
            (
                '(.*)donde(.*)rotonda(.*)',
                'La Rotonda del Titulo se encuentra a un costado de la Cafeteria. \n Aqui tienes la ubicacion: https://goo.gl/maps/TmsQenzZXwsvT9ib8'
            ),
            (
                '(.*)donde(.*)Titulacion(.*)',
                'La sala de Titulacion, de encuentra debajo de lso Edificios J, entrando por la 2 de agosto, todo derecho y primer edificio a la izquierda. \n Aqui tienes la ubicacion: https://goo.gl/maps/2ftZrVtuDEazSqu8A'
            ),
            (
                '(.*)(tramite|tramites)(.*)titulacion(.*)',
                'Aquí puedes encontrar información sobre los tramites de titualación \nhttps://www.tepic.tecnm.mx/tramites/titulacion'
            ),
            (
                '(.*)(tramite|tramites)(.*)ingreso(.*)',
                'Aquí puedes encontrar información sobre los tramites de nuevo ingreso \nhttps://www.tepic.tecnm.mx/aspirantes/nuevoingreso'
            ),
            (
                '(.*)(tramite|tramites)(.*)seguro(.*)',
                'Aquí puedes encontrar información sobre los tramites del seguro \nhttps://www.tepic.tecnm.mx/alumnos/seguro'
            ),
            (
                '(.*)(tramite|tramites)(.*)(afiliacion|imss)(.*)',
                'Aquí puedes encontrar información sobre los tramites del número de afiliación del IMSS \nhttps://www.tepic.tecnm.mx/alumnos/afiliacion'
            ),
            (
                '(.*)(becas|beca)(.*)cnbes(.*)',
                'Aquí puedes encontrar información sobre los tramites para la beca de CNBES \nhttp://www.cnbes.sep.gob.mx/'
            ),
            (
                '(.*)documentos(.*)servicio(.*)',
                'Aquí puedes encontrar información sobre los documentos para tu Servicio Social \n https://www.tepic.tecnm.mx/alumnos/documentos#servicio'
            ),
            (
                '(.*)reglamento(.*)',
                'Aquí puedes encontrar información sobre el reglamento para Alumnos \n https://www.tepic.tecnm.mx/doc/REGLAMENTO_PARA_ALUMNOS.pdf'
            ),
            (
                '(.*)documentos(.*)residencia(.*)',
                'Aquí puedes encontrar información sobre lso documentos para tu Residencia Profesional \n https://www.tepic.tecnm.mx/alumnos/documentos#residencia'
            ),
            (
                '(.*)(becas|beca)(.*)ingles(.*)',
                'Aquí puedes encontrar información sobre los tramites para la beca de inglés :3\nhttps://www.tepic.tecnm.mx/biblioteca/becas'
            ),
            (
                '(.*)(becas|beca)(.*)conacyt(.*)',
                'Aquí puedes encontrar información sobre los tramites para la beca del CONACYT :3\nhttp://www.conacyt.mx/index.php/becas-y-posgrados'
            ),
            (
                '(.*)(sitios|sitio)(.*)titulacion(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma EDDI2 :\nhttps://eddi2.ittepic.edu.mx/'
            ),
            (
                '(.*)(sitios|sitio)(.*)(correo|institucional)(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma del correo institucional :\nhttps://www.tepic.tecnm.mx/aspirantes/nuevoingreso'
            ),
            (
                '(.*)(sitios|sitio)(.*)sii(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma del SII :\nhttps://www.tepic.tecnm.mx/alumnos/seguro'
            ),
            (
                '(.*)(sitios|sitio)(.*)scg(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma del SGC :\nhttps://www.tepic.tecnm.mx/alumnos/afiliacion'
            ),
            (
                '(.*)(carrera|informacion)(.*)bioquimica(.*)',
                'Aquí puedes encontrar información sobre la carrera Ingenieria Bioquimica :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/ibq'
            ),
            (
                '(.*)(carrera|informacion)(.*)civil(.*)',
                'Aquí puedes encontrar información sobre la carrera Ingenieria Civil :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/ic'
            ),
            (
                '(.*)(carrera|informacion)(.*)arquitectura(.*)',
                'Aquí puedes encontrar información sobre la carrera Arquitectura :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/arq'
            ),
            (
                '(.*)(carrera|informacion)(.*)(electrica|electronica)(.*)',
                'Aquí puedes encontrar información sobre la carrera Ingenieria Electrica :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/ige'
            ),
            (
                '(.*)(carrera|informacion)(.*)gestion(.*)',
                'Aquí puedes encontrar información sobre la carrera de Ingeniería en Gestión Empresarial\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/ige'
            ),
            (
                '(.*)(carrera|informacion)(.*)industrial(.*)',
                'Aquí puedes encontrar información sobre la carrera de Ingeniería Industrial\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/ii'
            ),
            (
                '(.*)(carrera|informacion)(.*)mecatronica(.*)',
                'Aquí puedes encontrar información sobre la carrera de Ingeniería Mecatrónica\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/im'
            ),
            (
                '(.*)(carrera|informacion)(.*)quimica(.*)',
                'Aquí puedes encontrar información sobre la carrera de Ingeniería Química\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/iq'
            ),
            (
            '(.*)twitter(.*)',
            'Puedes estar al tanto de lo que se publica en el pefil de Twitter del ITTEPIC dando click en el siguiente enlace: \n Twitter: https://twitter.com/TecnmTepic'
            ),
            (
            '(.*)publicaciones(.*)',
            'Puedes estar al tanto de lo que se publica en el pefil de Twitter del ITTEPIC dando click en el siguiente enlace: \n Twitter: https://twitter.com/TecnmTepic.\n     O de las publicaciones del Facebook oficial del ITTEPIC dando click en el siguiente enlace: \n Facebook: https://www.youtube.com/user/TheARTE1999'
            ),
            (
            '(.*)youtube(.*)',
            'Puedes estar al tanto de los videos que se publican en YouTube sobre el ITTEPIC dando click en el siguiente enlace: : \n Youtube: https://www.youtube.com/user/TheARTE1999'
            ),
            (
            '(.*)videos(.*)',
            'Puedes estar al tanto de los videos que se publican en YouTube sobre el ITTEPIC dando click en el siguiente enlace: : \n Youtube: https://www.youtube.com/user/TheARTE1999'
            ),
            (
            '(.*)mensajes(.*)',
            'Puedes estar al tanto de las publicaciones del Facebook oficial del ITTEPIC dando click en el siguiente enlace: \n Facebook: https://www.facebook.com/TecnologicodeTepic/ '
            ),
            (
            '(.*)fotos(.*)',
            'Puedes estar al tanto de las publicaciones del Facebook oficial del ITTEPIC dando click en el siguiente enlace: \n Facebook: https://www.facebook.com/TecnologicodeTepic/'
            ),
            (
            '(.*)face(.*)',
            'Puedes estar al tanto de las publicaciones del Facebook oficial del ITTEPIC dando click en el siguiente enlace: \n Facebook: https://www.facebook.com/TecnologicodeTepic/'
            ),
            (
            '(.*)redes(.*)',
            'Sigue las redes de ITTEPIC: \n Twitter: https://twitter.com/TecnmTepic \n Youtube: https://www.youtube.com/user/TheARTE1999 \n Facebook: https://www.facebook.com/TecnologicodeTepic/'
            ),
            (
            '(.*)sociales(.*)',
            'Sigue las redes de ITTEPIC: \n Twitter: https://twitter.com/TecnmTepic \n Youtube: https://www.youtube.com/user/TheARTE1999 \n Facebook: https://www.facebook.com/TecnologicodeTepic/'
            ),
            (
                '(.*)(carrera|informacion)(.*)(sistemas|computacionales)(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma EDDI2 :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/isc'
            ),
            (
                '(.*)(carrera|informacion)(.*)(tecnologias|comunicacion)(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma del correo institucional :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/itic'
            ),
            (
                '(.*)(carrera|informacion)(.*)(licenciatura|administracion)(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma del SII :\nhttps://www.tepic.tecnm.mx/ofertaeducativa/licenciatura/la'
            ),
            (
                '(.*)(carrera|informacion)(.*)(alimentos|ciencias)(.*)',
                'Aquí puedes encontrar información sobre el sitio de la plataforma del SGC :\nhttps://www.tepic.tecnm.mx/posgrado/MCA/inicio'
            ),
            (
                'hola',
                self.first_message
            )
        ]
