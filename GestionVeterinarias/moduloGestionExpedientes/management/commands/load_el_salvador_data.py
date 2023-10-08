from django.core.management.base import BaseCommand
from moduloGestionExpedientes.models import Departamento, Municipio

class Command(BaseCommand):
    help = 'Carga datos de departamentos y municipios de El Salvador en la base de datos'

    def handle(self, *args, **kwargs):
        # Crea departamentos
        departamentos = [
            'Ahuachapán',
            'Cabañas',
            'Chalatenango',
            'Cuscatlán',
            'La Libertad',
            'La Paz',
            'La Unión',
            'Morazán',
            'San Miguel',
            'San Salvador',
            'San Vicente',
            'Santa Ana',
            'Sonsonate',
            'Usulután',
        ]
        for nombre in departamentos:
            departamento, created = Departamento.objects.get_or_create(nombre=nombre)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Departamento "{nombre}" creado.'))

        # Crea municipios asociados a los departamentos
        municipios = {
            'Ahuachapán': [
                'Ahuachapán',
                'Apaneca',
                'Atiquizaya',
                'Concepción de Ataco',
                'El Refugio',
                'Guaymango',
                'Jujutla',
                'San Francisco Menéndez',
                'San Lorenzo',
                'San Pedro Puxtla',
                'Tacuba',
                'Turín'
            ],
            'Cabañas': [
                'Cinquera',
                'Dolores',
                'Guacotecti',
                'Ilobasco',
                'Jutiapa',
                'San Isidro',
                'Sensuntepeque',
                'Tejutepeque',
                'Victoria'
            ],
            'Chalatenango': [
                'Chalatenango',
                'Arcatao',
                'Azacualpa',
                'Cancasque',
                'Citalá',
                'Comalapa',
                'Concepción Quezaltepeque',
                'Dulce Nombre de María',
                'El Carrizal',
                'El Paraíso',
                'La Laguna',
                'La Palma',
                'La Reina',
                'Las Vueltas',
                'Nueva Concepción',
                'Nueva Trinidad',
                'Ojos de Agua',
                'Potonico',
                'San Antonio de la Cruz',
                'San Antonio Los Ranchos',
                'San Fernando',
                'San Francisco Lempa',
                'San Francisco Morazán',
                'San Ignacio',
                'San Isidro Labrador',
                'San Luis del Carmen',
                'San Miguel de Mercedes',
                'San Rafael',
                'Santa Rita',
                'Tejutla',
                'Nombre de Jesús',
                'San Francisco Lempa'
            ],
            'Cuscatlán': [
                'Cojutepeque',
                'Aguilares',
                'Candelaria',
                'El Carmen',
                'El Rosario',
                'Monte San Juan',
                'Oratorio de Concepción',
                'San Bartolomé Perulapía',
                'San Cristóbal',
                'San José Guayabal',
                'San Pedro Perulapán',
                'San Rafael Cedros',
                'San Ramón',
                'Santa Cruz Analquito',
                'Santa Cruz Michapa',
                'Suchitoto',
                'Tenancingo',
                'San Lorenzo',
            ],
            'La Libertad': [
                'Santa Tecla',
                'Antiguo Cuscatlán',
                'Chiltiupán',
                'Ciudad Arce',
                'Colón',
                'Comasagua',
                'Huizúcar',
                'Jayaque',
                'Jicalapa',
                'La Libertad',
                'Nuevo Cuscatlán',
                'Opico',
                'Quezaltepeque',
                'Sacacoyo',
                'San José Villanueva',
                'San Juan Opico',
                'San Matías',
                'San Pablo Tacachico',
                'Talnique',
                'Tamanique',
                'Teotepeque',
                'Tepecoyo',
                'Zaragoza'
            ],
            'La Paz': [
                'Zacatecoluca',
                'Cuyultitán',
                'El Rosario',
                'Jerusalén',
                'Mercedes La Ceiba',
                'Olocuilta',
                'Paraíso de Osorio',
                'San Antonio Masahuat',
                'San Emigdio',
                'San Francisco Chinameca',
                'San Juan Nonualco',
                'San Juan Talpa',
                'San Juan Tepezontes',
                'San Luis La Herradura',
                'San Luis Talpa',
                'San Miguel Tepezontes',
                'San Pedro Masahuat',
                'San Pedro Nonualco',
                'San Rafael Obrajuelo',
                'Santa María Ostuma',
                'Santiago Nonualco',
                'Tapalhuaca'
            ],
            'La Unión': [
                'La Unión',
                'Anamorós',
                'Bolívar',
                'Concepción de Oriente',
                'Conchagua',
                'El Carmen',
                'El Sauce',
                'Intipucá',
                'Lislique',
                'Meanguera del Golfo',
                'Nueva Esparta',
                'Pasaquina',
                'Polorós',
                'San Alejo',
                'San José',
                'Santa Rosa de Lima',
                'Yayantique',
                'Yucuaiquín'
            ],
            'Morazán': [
                'San Francisco Gotera',
                'Arambala',
                'Cacaopera',
                'Chilanga',
                'Corinto',
                'Delicias de Concepción',
                'El Divisadero',
                'El Rosario',
                'Gualococti',
                'Guatajiagua',
                'Joateca',
                'Jocoaitique',
                'Jocoro',
                'Lolotique',
                'Meanguera',
                'Osicala',
                'Perquín',
                'San Carlos',
                'San Fernando',
                'San Isidro',
                'San Simón',
                'Sensembra',
                'Sociedad',
                'Torola',
                'Yamabal',
                'Yoloaiquín'
            ],
            'San Miguel': [
                'San Miguel',
                'Carolina',
                'Chapeltique',
                'Chinameca',
                'Chirilagua',
                'Ciudad Barrios',
                'Comacarán',
                'El Tránsito',
                'Lolotique',
                'Moncagua',
                'Nueva Guadalupe',
                'Nuevo Edén de San Juan',
                'Quelepa',
                'San Antonio del Mosco',
                'San Gerardo',
                'San Jorge',
                'San Luis de la Reina',
                'San Rafael Oriente',
                'Sesori',
                'Uluazapa'
            ],
            'San Salvador': [
                'San Salvador',
                'Aguilares',
                'Apopa',
                'Ayutuxtepeque',
                'Cuscatancingo',
                'Delgado',
                'El Paisnal',
                'Guazapa',
                'Ilopango',
                'Mejicanos',
                'Nejapa',
                'Panchimalco',
                'Rosario de Mora',
                'San Marcos',
                'San Martín',
                'Santiago Texacuangos',
                'Santo Tomás',
                'Soyapango',
                'Tonacatepeque'
            ],
            'San Vicente': [
                'San Vicente',
                'Apastepeque',
                'Guadalupe',
                'San Cayetano Istepeque',
                'San Esteban Catarina',
                'San Ildefonso',
                'San Lorenzo',
                'San Sebastián',
                'Santa Clara',
                'Santo Domingo',
                'Tecoluca',
                'Tepetitán',
                'Verapaz'
            ],
            'Santa Ana': [
                'Santa Ana',
                'Candelaria de la Frontera',
                'Chalchuapa',
                'Coatepeque',
                'El Congo',
                'El Porvenir',
                'Masahuat',
                'Metapán',
                'San Antonio Pajonal',
                'San Sebastián Salitrillo',
                'Santa Rosa Guachipilín',
                'Santiago de la Frontera',
                'Texistepeque'
            ],
            'Sonsonate': [
                'Sonsonate',
                'Acajutla',
                'Armenia',
                'Caluco',
                'Cuisnahuat',
                'Izalco',
                'Juayúa',
                'Nahuizalco',
                'Nahulingo',
                'Salcoatitán',
                'San Antonio del Monte',
                'San Julián',
                'Santa Catarina Masahuat',
                'Santa Isabel Ishuatán',
                'Santo Domingo de Guzmán',
                'Sonsonate',
                'Sonzacate'
            ],
            'Usulután': [
                'Usulután',
                'Alegría',
                'Berlín',
                'California',
                'Concepción Batres',
                'Ereguayquín',
                'Estanzuelas',
                'Jiquilisco',
                'Jucuapa',
                'Jucuarán',
                'Mercedes Umaña',
                'Nueva Granada',
                'Ozatlán',
                'Puerto El Triunfo',
                'San Agustín',
                'San Buenaventura',
                'San Dionisio',
                'San Francisco Javier',
                'Santa Elena',
                'Santa María',
                'Santiago de María',
                'Tecapán',
                'Usulután'
            ],
        }

        for departamento, municipios_list in municipios.items():
            dep_obj = Departamento.objects.get(nombre=departamento)
            for municipio in municipios_list:
                municipio_obj, created = Municipio.objects.get_or_create(nombre=municipio, departamento=dep_obj)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Municipio "{municipio}" creado en "{departamento}".'))

        self.stdout.write(self.style.SUCCESS('¡Datos de El Salvador cargados exitosamente!'))
