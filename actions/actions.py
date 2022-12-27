# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet

# #
class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_list"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Las manos de dios",
                        "subtitle": "Precios: Adultos $2, niños $1",
                        "image_url": "https://images.hive.blog/DQmQ2Gy7vYpNWFZMteM3EaPDyLjgdC5i3cFTWoWtTGMK7Xv/image.png",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/%22Las+Manos+de+Dios%22+Ba%C3%B1os+de+Agua+Santa/@-1.3786488,-78.4348441,17z/data=!4m5!3m4!1s0x91d391a051945545:0x1e2d2fbc28f64501!8m2!3d-1.378141!4d-78.4353729?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información manos de dios",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100063900711510",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Las manos de la Pachamama",
                        "subtitle": "Precios: $5 adultos y $2,50 niños",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5a2eff3112abd936197728c6/1626387639488-Z6SS8CMI39JUMF04SPWF/La+Mano+de+la+Pachamama+-+El+Vuelo+del+Condor+-+Banos+Ecuador.jpeg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/LA+MANO+DE+LA+PACHAMAMA/@-1.4119061,-78.4166448,17z/data=!4m5!3m4!1s0x91d3918bcddb68d1:0x6dc3f85d8e127eae!8m2!3d-1.4136115!4d-78.414352?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información manos de la Pachamama",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/elvuelodelcondorEC",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Puente de cristal en Baños",
                        "subtitle": "Precio: $7 por persona",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_35280.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Mega+Adventure+Park+R%C3%ADo+Blanco/@-1.3993073,-78.3489977,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39354abb33077:0xf040e636e8fffc47!8m2!3d-1.3993073!4d-78.3489977",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información puente de cristal",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/megaparkrioblanco",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de atractivos con mayor afluencia",attachment=new_carousel)
        return []

class ActionCarousel(Action):
    def name(self) -> Text:
        return "list_puentes"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Las manos de dios",
                        "subtitle": "Precios: Adultos $2, niños $1",
                        "image_url": "https://images.hive.blog/DQmQ2Gy7vYpNWFZMteM3EaPDyLjgdC5i3cFTWoWtTGMK7Xv/image.png",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/%22Las+Manos+de+Dios%22+Ba%C3%B1os+de+Agua+Santa/@-1.3786488,-78.4348441,17z/data=!4m5!3m4!1s0x91d391a051945545:0x1e2d2fbc28f64501!8m2!3d-1.378141!4d-78.4353729?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información manos de dios",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100063900711510",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Las manos de la Pachamama",
                        "subtitle": "Precios: $5 adultos y $2,50 niños",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5a2eff3112abd936197728c6/1626387639488-Z6SS8CMI39JUMF04SPWF/La+Mano+de+la+Pachamama+-+El+Vuelo+del+Condor+-+Banos+Ecuador.jpeg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/LA+MANO+DE+LA+PACHAMAMA/@-1.4119061,-78.4166448,17z/data=!4m5!3m4!1s0x91d3918bcddb68d1:0x6dc3f85d8e127eae!8m2!3d-1.4136115!4d-78.414352?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "manos de la Pachamama",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/elvuelodelcondorEC",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Puente de cristal en Baños",
                        "subtitle": "Precio: $7 por persona",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_35280.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Mega+Adventure+Park+R%C3%ADo+Blanco/@-1.3993073,-78.3489977,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39354abb33077:0xf040e636e8fffc47!8m2!3d-1.3993073!4d-78.3489977",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información puente de cristal",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/megaparkrioblanco",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Los Pies de Dios",
                        "subtitle": "Precio: $2",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t39.30808-6/281362098_156223570268463_3917025565137347655_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=a26aad&_nc_eui2=AeGZet7D-vEelFU4AyAj6lItzi2i-NNJGYbOLaL400kZhgE2kwsPhGNDqZ4kevRXlm_o6C7dbUOkikvMkMONPSnl&_nc_ohc=NJiIUFELRKkAX-4Ywn1&_nc_ht=scontent.fatf4-1.fna&oh=00_AfCSskVjIQ9wb9zPioIE0nICWBBkpDlI8CtFlNqrZJtkiA&oe=63A37E74",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Mirador+Los+Pies+de+Dios/@-1.3801102,-78.4362743,18z/data=!4m5!3m4!1s0x91d391879e7356d7:0x3db0a0abbdc09796!8m2!3d-1.3797852!4d-78.4358587",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información pies de dios",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/lospiesdedios",
                            "type": "web_url"
                            }
                        ]
                    },
                ]
                }
        }
        dispatcher.utter_message(text="Lista de atractivos: Puentes",attachment=new_carousel)
        return []

class ActionCarousel(Action):
    def name(self) -> Text:
        return "Columpios_lista"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Columpio Fantasías de Volar",
                        "subtitle": "Precios: $  10 por persona",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/12/3a/ef/5d/volando-sobre-banos-de.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Columpio+Fantasias+De+Volar/@-1.408059,-78.424434,15z/data=!4m5!3m4!1s0x91d391293662b1f9:0x8e02011f4a7c3c24!8m2!3d-1.408059!4d-78.424434?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información fantasias de volar",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100047005794637",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Casa del árbol",
                        "subtitle": "Precios: e $1 por persona",
                        "image_url": "https://i.pinimg.com/originals/09/44/c8/0944c8a8a067ebb71458e2b8626339b7.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/La+Casa+del+Arbol/@-1.4182111,-78.4263339,17z/data=!3m1!4b1!4m5!3m4!1s0x91d396d429a823e3:0x88718e7ae34cd3a5!8m2!3d-1.4182111!4d-78.4263339?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información casa del árbol",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/lacasadelarbolec",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "El vuelo del cóndor",
                        "subtitle": "Precio: $10 por persona",
                        "image_url": "https://goecuador.net/archivos/minegocio/el-vuelo-del-condor-banos-de-agua-santa-ecuador_2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/LA+MANO+DE+LA+PACHAMAMA/@-1.4119061,-78.4166448,17z/data=!4m5!3m4!1s0x91d3918bcddb68d1:0x6dc3f85d8e127eae!8m2!3d-1.4136115!4d-78.414352?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información vuelo del cóndor",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/elvuelodelcondorEC",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "columpio extremo el abismo del diablo",
                        "subtitle": "Precio: $10 por persona",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t1.6435-9/123370627_634293370579396_2611973146868467534_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8bfeb9&_nc_eui2=AeEkEwbtja3l4WA0Puk9Jg-pzsOnH-gMe8bOw6cf6Ax7xpKGOoCOOnQHRJXh6dQ2b-nseDK269G20a-9ScILaHYm&_nc_ohc=QhKY74QPaP4AX-2Y6Vo&_nc_ht=scontent.fatf4-1.fna&oh=00_AfCrKiBc7TwfsaMEupHU13HhiIkcgAtrShHzvE_3FUinuQ&oe=63C1A362",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/COLUMPIO+EXTREMO+EL+ABISMO+DEL+DIABLO/@-1.402961,-78.298772,18z/data=!4m5!3m4!1s0x0:0xfbdccc75cc695000!8m2!3d-1.4035169!4d-78.2977725?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información abismo del diablo",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100067229470150",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de columpios",attachment=new_carousel)
        return []
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_weather"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         city = tracker.get_slot('location')
#         temperature=Weather(city)['temp']
#         response = "The current temperature at {} is {} degree Celsius.".format(city,temperature)
#         dispatcher.utter_message(response)
#         return [SlotSet('location',city)]

# # action name
# class ActionSayShirtSize(Action):

#     def name(self) -> Text:
#         return "action_say_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name = tracker.get_slot("name")
#         if not name:
#             dispatcher.utter_message(text="No sé tu nombre")
#         else:
#             dispatcher.utter_message(text=f"¡Hola! Encantado de conocerte {name}!")
#         return []

class ActionCarousel(Action):
    def name(self) -> Text:
        return "visitar_cascadas"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "El manto de la novia",
                        "subtitle": "Canopy: $10 por persona, Tarabita:$3 a $5",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/1c/e8/e4/5f/caption.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Cascada+Manto+de+la+Novia/@-1.4038417,-78.3355075,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3935b9ecfb70b:0xc1dfa16ac3d791df!8m2!3d-1.4038417!4d-78.3355075?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información manto de la novia",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Cascada de Agoyán",
                        "subtitle": "Canopy: $10 por persona, Tarabita:$3 a $5",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/16/6c/9b/b7/cascada-de-agoyan-banos.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/1%C2%B023'56.7%22S+78%C2%B022'10.6%22W/@-1.3990833,-78.3696111,17z/data=!3m1!4b1!4m6!3m5!1s0x0:0xcca17d10913a164e!7e2!8m2!3d-1.3990876!4d-78.3696065?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información cascada agoyan",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "El pailón del diablo",
                        "subtitle": "Precio: $2,50",
                        "image_url": "https://www.laflorestahotel.com/archivos/blogs/pailon-del-diablo-banos-ecuador.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Cascada+El+Pailon+(del+Diablo)/@-1.4044668,-78.297827,17z/data=!3m1!4b1!4m5!3m4!1s0x91d393fc6b20ad6d:0xbfc06a78c4bded53!8m2!3d-1.4044668!4d-78.297827",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "El pailón del diablo",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Cascada de la Virgen",
                        "subtitle": "Precio: $0",
                        "image_url": "https://c8.alamy.com/comp/2DR01F2/shrine-of-the-holy-mary-virgen-del-rosario-de-agua-santa-at-the-waterfall-cascada-manto-de-la-novia-banos-de-agua-santa-tungurahua-province-2DR01F2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Cascada+de+la+Virgen/@-1.3991067,-78.4196862,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3913cba4fe99f:0x9098e08ddb2d3d9f!8m2!3d-1.3991067!4d-78.4174975?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información cascada virgen",
                            "type": "postback"
                            }
                        ]
                    }, 
                    {
                        "title": "Cascada Inés María",
                        "subtitle": "Precio: $0",
                        "image_url": "https://s2.wklcdn.com/image_125/3750282/23303233/14787740.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Cascada+In%C3%A9s+Mar%C3%ADa+Ba%C3%B1os+Tungurahua/@-1.3957613,-78.4359408,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391f086f24d7b:0x9276d5515be8279!8m2!3d-1.3957613!4d-78.4359408?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información cascada ines maria",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Cascada San Antonio",
                        "subtitle": "Precio: $0",
                        "image_url": "http://www.southamericanpostcard.com/images/photos/ecuador-FABU3823_trip7.JPG",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Cascada+del+Silencio/@-1.4004158,-78.4006583,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3914274759349:0x6bbf01636ad0542e!8m2!3d-1.4004158!4d-78.4006583?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información cascada san antonio",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Cascada de Chamana",
                        "subtitle": "Precio: $0",
                        "image_url": "https://static.wixstatic.com/media/47d72f_d1ca7f265b0c4669a82797be9ddc9b5a~mv2_d_3024_3780_s_4_2.jpg/v1/fill/w_740,h_925,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/47d72f_d1ca7f265b0c4669a82797be9ddc9b5a~mv2_d_3024_3780_s_4_2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Las+cascadas+de+chamana+y+ulbilla/@-1.4011036,-78.4101904,15z/data=!4m10!1m2!2m1!1sCascada+de+Chamana!3m6!1s0x91d3910b102e7401:0x839bf12cd93ca9e6!8m2!3d-1.4012667!4d-78.4002409!15sChJDYXNjYWRhIGRlIENoYW1hbmGSAQtoaWtpbmdfYXJlYeABAA!16s%2Fg%2F11k3rrpz01?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información chamana",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de las principales cascadas de la ciudad",attachment=new_carousel)
        return []



class ActionCarousel(Action):
    def name(self) -> Text:
        return "medios_trasportes"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Alquiler bicicletas",
                        "subtitle": "Precios: $10",
                        "image_url": "https://2.bp.blogspot.com/-rET5ZputVAo/Vu9hkFUP7OI/AAAAAAAAJt4/c4JcCKw7LL0YWDrqnfbmlCxyif0E3i49Q/s1600/diversion_1.jpg",
                        "buttons": [ 
                            {
                            "title": "Alquilar",
                            "payload": "alquiler",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información renta",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Alquiler Cuadrones",
                        "subtitle": "Precio: $15",
                        "image_url": "https://www.imagineecuador.com/wp-content/uploads/2021/10/Recurso-125-2.png",
                        "buttons": [ 
                            {
                            "title": "Alquilar",
                            "payload": "alquiler",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información renta",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Alquiler Buggy",
                        "subtitle": "Precio: $15",
                        "image_url": "https://www.chetoba.com.ar/wp-content/uploads/karting-banos-ecuador.jpg",
                        "buttons": [ 
                            {
                            "title": "Alquilar",
                            "payload": "alquiler",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información renta",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Alquiler Motocicletas",
                        "subtitle": "Precio: $15",
                        "image_url": "https://scontent.fuio13-1.fna.fbcdn.net/v/t1.6435-9/71224932_2392671980786439_7529513591888674816_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=9267fe&_nc_eui2=AeHbLZyGWpl3OHAA5xsnCldo_Mf4cdhPW-r8x_hx2E9b6rDbRu-oNkd1BiUdjqouDPuMtOYUy1YG_IkKVeYBFKTP&_nc_ohc=IDPpY5aSv6wAX8e__OK&_nc_ht=scontent.fuio13-1.fna&oh=00_AfAgjMVM1yiIKiH88EOJdxnan58ZB8gpCmblmSwlcaY1Rw&oe=63C05A09",
                        "buttons": [ 
                            {
                            "title": "Alquilar",
                            "payload": "alquiler",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información renta",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Alquiler Jeep",
                        "subtitle": "Precio: $20",
                        "image_url": "https://hare-media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/0b/fd/25/90.jpg",
                        "buttons": [ 
                            {
                            "title": "Alquilar",
                            "payload": "alquiler",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información renta",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="¡El precio de alquiler varia en cada agencia!",attachment=new_carousel)
        return []

class ActionCarousel(Action):
    def name(self) -> Text:
        return "extremo_list"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    # {
                    #     "title": "Parapente",
                    #     "subtitle": "Precio: $150 por persona",
                    #     "image_url": "https://goecuador.net/archivos/blogs/parapente-banos-ecuador_1.jpg",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Whatsapp",
                    #         "url": "https://api.whatsapp.com/message/RAQEGXCRT5YEF1?autoload=1&app_absent=0",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "más información paramente",
                    #         "type": "postback"
                    #         },
                    #         {
                    #         "title": "Redes sociales",
                    #         "url": "https://www.instagram.com/cabros_outdoor/",
                    #         "type": "web_url"
                    #         }
                    #     ]
                    # },
                    {
                        "title": "Rafting",
                        "subtitle": "Precio: $ 30 por persona",
                        "image_url": "https://samarispa.com/wp-content/uploads/2021/05/WhatsApp-Image-2021-06-03-at-9.12.52-AM-1024x576.jpeg",
                        "buttons": [ 
                            {
                            "title": "Más información",
                            "payload": "rafting",
                            "type": "postback"
                            },
                            {
                            "title": "Dónde contratar actividad",
                            "payload": "contratar rafting",
                            "type": "postback"
                            },
                            {
                            "title": "Precio",
                            "payload": "precio rafting",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Canyoning",
                        "subtitle": "Precio: $30 por persona",
                        "image_url": "http://banosecuador.com/wp-content/uploads/2011/12/Team-Adventure-Canyoning.jpg",
                        "buttons": [
                            {
                            "title": "Más información",
                            "payload": "canyoning",
                            "type": "postback"
                            },
                            {
                            "title": "Dónde contratar actividad",
                            "payload": "contratar canyonin",
                            "type": "postback"
                            },
                            {
                            "title": "Precio",
                            "payload": "precio canyoning",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Escalada en roca",
                        "subtitle": "Precio: $30 por persona",
                        "image_url": "https://www.imagineecuador.com/wp-content/uploads/2021/11/Recurso-114-e1637340114259.png",
                        "buttons": [
                            {
                            "title": "Más información",
                            "payload": "escalada en roca ",
                            "type": "postback"
                            },
                            {
                            "title": "Dónde contratar actividad",
                            "payload": "contratar escalada en roca ",
                            "type": "postback"
                            },
                            {
                            "title": "Precio",
                            "payload": "precio escalada en roca",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Salto de puente",
                        "subtitle": "Precio: $20 por persona",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5d23b57617786c0001fcbeda/1572634731708-3FHOE9ODR6AJCFPVQ213/Salto-del-puente---puenting---San-Francisco---Banos.jpg",
                        "buttons": [
                            {
                            "title": "Más información",
                            "payload": "salto de puente",
                            "type": "postback"
                            },
                            {
                            "title": "Dónde contratar actividad",
                            "payload": "contratar salto de puente",
                            "type": "postback"
                            },
                            {
                            "title": "Precio",
                            "payload": "precio salto de puente ",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de actividades extremas",attachment=new_carousel)
        return []


class ActionCarousel(Action):
    def name(self) -> Text:
        return "zoo_listas"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Vida Exótica San Martín",
                        "subtitle": "Precio: $3 adultos, $2 niños",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_31318.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Zoo+Vida+Ex%C3%B3tica/@-1.3964769,-78.4371854,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39132e15856eb:0x3d22b5c776b39ea5!8m2!3d-1.3964769!4d-78.4371854?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "vida exotica",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/zoovidaexotika",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "EcoZoo San Martín",
                        "subtitle": "Precio: $4 adultos, $3 niños",
                        "image_url": "http://ecozoosanmartin.com/wp-content/uploads/2013/06/OsodeAnteojosZooEcuador-800x400.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Eco+zool%C3%B3gico+San+Mart%C3%ADn/@-1.396424,-78.4368971,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39169fd59315f:0xd51a7cbb561db913!8m2!3d-1.396424!4d-78.4368971",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "El zoológico san martin",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/ecozoologicosanmartinecuador",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de zoológicos de la ciudad",attachment=new_carousel)
        return []


class ActionCarousel(Action):
    def name(self) -> Text:
        return "gastronomia"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "La fábrica de chocolate en Baños",
                        "subtitle": "Precio: $0",
                        "image_url": "https://trafficamerican.com/wp-content/uploads/2022/06/fabrica-de-chocolate-3-1024x576.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/F%C3%A1brica+M%C3%A1gica+de+Chocolate/@-1.4009024,-78.4227217,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3910a2606524f:0x3db57affb6a3d064!8m2!3d-1.4009024!4d-78.4227217?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información frabrica de chocolate",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/FabricaMagicadeChocolate",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de atractivos gastronómicos",attachment=new_carousel)
        return []

class ActionCarousel(Action):
    def name(self) -> Text:
        return "List_parques"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "El bosque encantado",
                        "subtitle": "Precio: $4 adultos, $2 niños",
                        "image_url": "https://trafficamerican.com/wp-content/uploads/2022/07/ATRACCION-2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/El+Bosque+Encantado/@-1.4018859,-78.4253846,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912542817999:0x210785788b6a7fb6!8m2!3d-1.4018859!4d-78.4231906?hl=es&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "bosque encandado",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/ElBosqueEncantadoEC/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Animal Park",
                        "subtitle": "Precio: $6 adultos, $3 niños",
                        "image_url": "https://animalpark.ec/wp-content/uploads/2021/04/slide-2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/ANIMALPARK+PARQUE+TEM%C3%81TICO/@-1.4101985,-78.415867,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3916adbe54ee5:0x2f996013fff3d1a!8m2!3d-1.4101985!4d-78.415867",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información animal park",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/AnimalPark-1033209876818756/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Discovery Baños",
                        "subtitle": "Precio: de $1 a $5",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-o/08/9f/ad/bb/discovery-banos.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Discovery+Ba%C3%B1os/@-1.3990065,-78.3801008,15z/data=!4m5!3m4!1s0x91d3936f1357ab43:0x853303c8b1a8dcdd!8m2!3d-1.398129!4d-78.3671952",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información discovery baños",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/discoverybanos",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Parque de aventuras de San Martín",
                        "subtitle": "Precio: $20 por persona",
                        "image_url": "https://img.goraymi.com/2019/11/18/4c72d92de5c7f8c4a1d2961c442c59df_lg.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/PARQUE+AVENTURA+SAN+MARTIN/@-1.3949785,-78.4380035,17z/data=!3m1!4b1!4m5!3m4!1s0x91d390e7923fe599:0xcff71819fb57a886!8m2!3d-1.3949785!4d-78.4380035",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información parque aventura san martin",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100083143339774",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Parque de dinosaurios",
                        "subtitle": "Precio: $6 adultos y $3,50 niños",
                        "image_url": "https://directorio593.com/custom/domain_1/image_files/1080_photo_29926.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Dinosaurios+Park/@-1.4007348,-78.4105307,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3916d35e154f9:0x6c309bd68abe918d!8m2!3d-1.4007348!4d-78.4105307",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información parque dinosaurios",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/DinosauriosPark",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Parque temático Pueblos del mundo",
                        "subtitle": "Precio: $3",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t39.30808-6/287528743_3068283230153316_7006248754419818901_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHjAUZX5XiMq_GnpqKTvfWCkiz_9vdYKYKSLP_291gpgjWgqJeKcRfn8PO8X7AKUkc7k99BeKoIO9ziCkgNNFCN&_nc_ohc=nFj4f8z4auMAX8rqm6y&_nc_ht=scontent.fatf4-1.fna&oh=00_AfC5m87ou135clc58hFtAflI2qen2PELBbZ2SD_zUEaTxw&oe=63ADE45B",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Dinosaurios+Park/@-1.4007348,-78.4105307,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3916d35e154f9:0x6c309bd68abe918d!8m2!3d-1.4007348!4d-78.4105307",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información pueblos del mundo",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/PueblodelMundo",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "PiQchur Parque fotográfico",
                        "subtitle": "Precio: $3 adultos y $2 niños",
                        "image_url": "https://directorio593.com/custom/domain_1/image_files/sitemgr_photo_35746.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/piQchur/@-1.3808585,-78.4309264,15.74z/data=!4m5!3m4!1s0x91d3916227fcf88f:0x931dfc6c796985c6!8m2!3d-1.379453!4d-78.4364488?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información piqchur",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/piqchuroficial/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "La Aldea Mágica",
                        "subtitle": "Precio: $3 adultos y $1,5 niños",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-o/15/50/31/1d/duende-de-arbol.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/La+Aldea+M%C3%A1gica/@-1.3922608,-78.4172929,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391bfa7b2cd93:0xb6f725d561390841!8m2!3d-1.3922608!4d-78.4172929",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información aldea magica",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/LaAldeaMagicaPAGINAOFICIAL/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Troll Mountain cine al aire libre",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://casasholidayhomes.com/images/blog_turismo/troll/troll.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Troll+Mountain/@-1.3927375,-78.4246551,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912503a0a119:0x8ef81b133fb67ac2!8m2!3d-1.3927375!4d-78.4246551",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información troll mountain",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/trollmountain.ec/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Cavernas Sigsi Huayco",
                        "subtitle": "Precio: $3",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_39768.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Caverna+Sigsi+-+Huayco/@-1.3943394,-78.421789,17z/data=!4m5!3m4!1s0x91d39165212546c9:0x42e1a13b977e0b55!8m2!3d-1.3943391!4d-78.4217909?hl=es-EC",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "cavernas Sigsi Huayco",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/cavernasigsihuayco/?show_switched_toast=0&show_invite_to_follow=0&show_switched_tooltip=0&show_podcast_settings=0&show_community_transition=0&show_community_review_changes=0&show_community_rollback=0&show_follower_visibility_disclosure=0",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de Parques temáticos",attachment=new_carousel)
        return []
#Miradores
class ActionCarousel(Action):
    def name(self) -> Text:
        return "listar_miradores"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Los Pies de Dios",
                        "subtitle": "Precio: $2",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipNt6PT8_hsKRx64GrWmlmJBjC6pjtW7XBZieP31=w768-h768-n-o-v1",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Mirador+Los+Pies+de+Dios/@-1.3801102,-78.4362743,18z/data=!4m5!3m4!1s0x91d391879e7356d7:0x3db0a0abbdc09796!8m2!3d-1.3797852!4d-78.4358587",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información pies de dios",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/lospiesdedios",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Sacha 360º Mirador & Café",
                        "subtitle": "Precio: $2",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipP-AxU9wTNJvSp3dMDG15KzEFm7kvKoMhg0YLCQ=s680-w680-h510",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Mirador+Bellavista/@-1.4000673,-78.4141538,17.74z/data=!4m5!3m4!1s0x91d3913c1d36eb8b:0x2c9e1347581728e7!8m2!3d-1.3998779!4d-78.4145889?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "Mirador Sacha 360",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/sacha.360",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Mirador de Bellavista",
                        "subtitle": "Precio: 50 centavos",
                        "image_url": "https://www.georges-backpackingguides.com/wp-content/uploads/2022/06/Mirador.Banos_.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Mirador+Bellavista/@-1.4000673,-78.4141538,17.74z/data=!4m5!3m4!1s0x91d3913c1d36eb8b:0x2c9e1347581728e7!8m2!3d-1.3998779!4d-78.4145889?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información mirador bellavista",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Café Giratorio",
                        "subtitle": "Precio: $3 ",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/1c/bb/3c/3e/20210225-105848-largejpg.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Caf%C3%A9+Giratorio/@-1.3974038,-78.4170547,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391aae1cbe637:0x217849fcd907495d!8m2!3d-1.3974038!4d-78.4148607?hl=es&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información cafe giratorio",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100083339372432",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "El Beso de la Luna",
                        "subtitle": "Precio: $1",
                        "image_url": "https://www.imagineecuador.com/wp-content/uploads/2021/10/Recurso-93-8.png",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/El+Beso+de+la+Luna/@-1.3788181,-78.4392336,17z/data=!4m5!3m4!1s0x91d391e38590ac21:0xb4f3a3c3f315ba41!8m2!3d-1.3788181!4d-78.4370449?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "más información beso de la luna",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100076001416193",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Mirador Ojos Del Volcán-Nido Del Águila",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipNsJpRk-xpUaLKWixLSzuMjXajnoKupBJpyHMYQ=w960-h960-n-o-v1",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Mirador+ojos+del+volcan-nido+del+%C3%A1guila/@-1.3841049,-78.4375218,20z/data=!4m5!3m4!1s0x91d391beeaec81b5:0xa4dc9d7b99120599!8m2!3d-1.3839639!4d-78.4375822",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "nido del aguila",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/refugioojosdelvolcan",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Ventana de Kong",
                        "subtitle": "Precio: $2",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_41480.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/El+Ventanal+de+Kong/@-1.3838545,-78.4369699,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391870480f17f:0x81915689d7b2ce1f!8m2!3d-1.3838545!4d-78.4369699?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "ventanal de kong",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100075968306264",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Cristo Redentor",
                        "subtitle": "Precio: $2",
                        "image_url": "https://www.turismoecuador24.com/archivos/destinos/cristo_redentor-turismo_ecuador_24.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Cristo+Redentor+de+Ba%C3%B1os+de+Agua+Santa/@-1.3829375,-78.4360625,17z/data=!4m5!3m4!1s0x91d3917bd42d0fcd:0x778f7ccec5dde38c!8m2!3d-1.3829375!4d-78.4360625",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "cristo redentor",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100078904175317",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de miradores de la ciudad",attachment=new_carousel)
        return []
# Fin miradores

# piscinas
class ActionCarousel(Action):
    def name(self) -> Text:
        return "existencia_piscinas"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Piscinas de la Virgen",
                        "subtitle": "Precio: $4 adultos y $2 niños",
                        "image_url": "https://i.pinimg.com/originals/17/f2/c4/17f2c40b4f48b539cd9385f704443bed.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Termas+de+la+Virgen/@-1.3982652,-78.4202581,17z/data=!4m5!3m4!1s0x91d39122c52c61fd:0xfaa0f21baa970208!8m2!3d-1.3987719!4d-78.4175783?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas de la virgen",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Termas de la Virgen",
                        "subtitle": "Precio: $6 adultos y $3 niños",
                        "image_url": "https://img.goraymi.com/2018/11/15/e5bc0af5084578b889a30f0cf7e16896_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Piscinas+Termas+De+La+Virgen+-+Ba%C3%B1os+Ecuador/@-1.3982652,-78.4202581,17z/data=!4m5!3m4!1s0x0:0x4c067c5ae04d1cd4!8m2!3d-1.3981689!4d-78.4185118?hl=es&shorturl=1&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas de las termas de la virgen",
                            "type": "postback"
                            }
                        ]
                    }
                    # ,
                    # {
                    #     "title": "El Refugio Spa Garden",
                    #     "subtitle": "Precio: $17 adultos y $12 niños",
                    #     "image_url": "https://elrefugiospa.com/wp-content/uploads/2022/03/Piscina7.jpg",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Cómo llegar",
                    #         "url": "https://www.google.com/maps/place/El+Refugio+Spa+Garden/@-1.3919899,-78.4122686,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391142ded7493:0xb73a9c8c908e6426!8m2!3d-1.3919899!4d-78.4100799?hl=es-419&shorturl=1",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "más información refugio spa garden",
                    #         "type": "postback"
                    #         },
                    #         {
                    #         "title": "Redes sociales",
                    #         "url": "https://www.facebook.com/elrefugiospa/",
                    #         "type": "web_url"
                    #         }
                    #     ]
                    # }
                    ,
                    {
                        "title": "Piscina de Santa Clara",
                        "subtitle": "Precio: $4 adultos y $2 niños",
                        "image_url": "https://img.goraymi.com/2018/11/15/974392d06c3f723d04e88225e08b35c1_lg.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Balneario+Santa+Clara+(El+Cangrejo)/@-1.3979118,-78.4213715,17z/data=!4m5!3m4!1s0x0:0x5103de56b1fb15b6!8m2!3d-1.4006486!4d-78.4193153?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas santa clara",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Termales El Salado",
                        "subtitle": "Precio: $3 adultos y $1,5 niños",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5d23b57617786c0001fcbeda/1572902830025-QDYPG9EQJPRM0XAJ5PS4/Termas%2BEl%2BSalado%2BBanos%2B2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Balneario+El+Salado/@-1.402449,-78.436153,16z/data=!4m5!3m4!1s0x91d390d82c079589:0x3a89a5ac6ad94ee6!8m2!3d-1.4045738!4d-78.4323045?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas el salado ",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Piscina de Santa Ana",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://img.goraymi.com/2018/11/15/d2de0f2f75de9f27db3d115f912eb2d1_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Complejo+Santa+Ana/@-1.3955988,-78.4113088,17z/data=!4m5!3m4!1s0x91d3913fd7090945:0xa536512b9305557!8m2!3d-1.3953593!4d-78.4092785?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas santa ana",
                            "type": "postback"
                            }
                        ]
                    }
                    # ,
                    # {
                    #     "title": "Quinta los Juanes Pool",
                    #     "subtitle": "Precio: $20 adultos y $10 niños",
                    #     "image_url": "https://directorio593.com/custom/domain_1/image_files/sitemgr_photo_32987.jpg",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Cómo llegar",
                    #         "url": "https://www.google.com/maps/place/Quinta+Los+Juanes/@-1.3984921,-78.4387563,17z/data=!3m1!4b1!4m8!3m7!1s0x91d3916b4e5ff6d3:0x498635e5be2f5c42!5m2!4m1!1i2!8m2!3d-1.3984921!4d-78.4387563",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "más información quinta los juanes",
                    #         "type": "postback"
                    #         },
                    #         {
                    #         "title": "Redes sociales",
                    #         "url": "https://www.facebook.com/hotelquintalosjuanes",
                    #         "type": "web_url"
                    #         }
                    #     ]
                    # }
                    # ,
                    # {
                    #     "title": "Complejo Eduardos",
                    #     "subtitle": "Precio Spa: $10 adultos y $5 niños",
                    #     "image_url": "https://goecuador.net/archivos/minegocio/complejo-eduuardos-banos-ecuador-dinos-park_10.jpg",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Cómo llegar",
                    #         "url": "https://www.google.com.ec/maps/place/Eduardo's+Ecolog%C3%ADa+%26+Aventura/@-1.4009557,-78.4216241,17z/data=!4m5!3m4!1s0x91d391249464efd1:0xc3be520fd6ae6425!8m2!3d-1.4008597!4d-78.4200739?hl=es",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "más información complejo eduardos",
                    #         "type": "postback"
                    #         },
                    #         {
                    #         "title": "Redes sociales",
                    #         "url": "https://www.facebook.com/Eduardos.Ecologia.y.Aventura",
                    #         "type": "web_url"
                    #         }
                    #     ]
                    # }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de las principales piscinas de la ciudad",attachment=new_carousel)
        return []

# fin piscinas

# museos
class ActionCarousel(Action):
    def name(self) -> Text:
        return "conteo_museos"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Museo Fray Enrique Mideros",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://img.goraymi.com/2018/06/15/50d5c37f048b430a3c3c78a98c8cbd68_lg.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Museo+Fray+Enrique+Mideros/@-1.3973952,-78.4210431,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39122fe8dffd5:0xafb55ec348545273!8m2!3d-1.3973952!4d-78.4210431?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "museo juan enrique mideros",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/profile.php?id=100064109942493",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de museos de la ciudad",attachment=new_carousel)
        return []

# fin museos
class ActionCarousel(Action):
    def name(self) -> Text:
        return "senderos_banios"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Baños Bellavista",
                        "subtitle": "Precios: $0,50",
                        "image_url": "https://th.bing.com/th/id/R.bcb30384c27819ec4f3708d362e9223d?rik=j3D3V0r3oDp%2bhA&riu=http%3a%2f%2f1.bp.blogspot.com%2f-sLkfaGJhvg8%2fU1RZgRbQdDI%2fAAAAAAAACcs%2f46T7AzGA8ro%2fs1600%2fDSC_0408_EatPrayCureTravel.JPG&ehk=gdM3eLaWN%2fK7XE%2fkQvyyyeG4TNN5eEoj9%2b8us6YRSis%3d&risl=&pid=ImgRaw&r=0",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/mirador-la-cruz-bellavista?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 2.7 KM",
                            "payload": "sendero Bellavista",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "sendero Bellavista",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Baños Illuchi Sauces",
                        "subtitle": "Precio: $ 0",
                        "image_url": "https://s2.wklcdn.com/image_120/3605816/55576940/37153943.700x525.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/sendero-de-los-sauces?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 6.8 KM",
                            "payload": "camino de los sauces",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "camino de los sauces",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Baños la Virgen",
                        "subtitle": "Precio: $0",
                        "image_url": "https://c8.alamy.com/compes/f52n4d/banos-canton-es-un-canton-de-ecuador-ubicada-en-la-provincia-de-tungurahua-vista-desde-el-mirador-de-la-virgen-f52n4d.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/monumento-a-la-virgen-de-banos?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 1.3 KM",
                            "payload": "mirador de la virgen",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "mirador la virgen",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Baños Pondoa",
                        "subtitle": "Precio: $ 0",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t1.6435-9/196548864_2130913640540454_2609577053806143772_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeEyeczG7tA_cAhCLeMu8ZK8GO7g8uZozgcY7uDy5mjOBykjh_n8Xshudnogdw1PR-d0XFVFxCh7q6lGUV_5NaRz&_nc_ohc=9G8EPfKfBEcAX-A35RI&_nc_ht=scontent.fatf4-1.fna&oh=00_AfDgZ3rf9j7pg8DiK2fzeF1ehW7TolgQhE07Hd0Ge-Ppxg&oe=63C0E286",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Sendero+a+Pondoa/@-1.4007698,-78.4364347,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391d6436e7e6f:0x1c32fa521ad578f!8m2!3d-1.4007752!4d-78.434246",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 2.8 KM",
                            "payload": "inforación sendero pondoa",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "inforación sendero pondoa",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Baños Luna Vólcan",
                        "subtitle": "Precio: $0",
                        "image_url": "https://s2.wklcdn.com/image_106/3201816/31932374/20536574Master.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://es.wikiloc.com/rutas-senderismo/banos-luna-volcan-mirador-de-la-virgen-banos-a-bajo-ritmo-81822619",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 5.9 KM",
                            "payload": "luna volcan sendero",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "luna volcan sendero",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "La virgen y Casa del árbol",
                        "subtitle": "Precio: $0",
                        "image_url": "https://www.santacruzbackpackers.com/archivos/blogs/mirador-banos.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/torre-al-cielo-y-casa-del-arbol?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 6.3 KM",
                            "payload": "sendero a la casa del arbol",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "sendero a la casa del arbol",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Ruta de los Contrabandistas",
                        "subtitle": "Precio: $0",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t1.6435-9/37737585_233076270667185_1514949331688357888_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_eui2=AeEWqZM7XUKKPDsBmJVdFYc9JVBCoqD0gD4lUEKioPSAPpsnXopNzYxj4redVQ5VZJdWRktURc4g1d6BqkoPQXEi&_nc_ohc=kNg6ypTInMsAX-IFRsL&_nc_ht=scontent.fatf4-1.fna&oh=00_AfCVYdF1TnHdzE4yeYE2NPI6xkMMXK-UDsLv4QSDVA5RLg&oe=63C0EEA4",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/sendero-de-los-contrabandistas?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distancia: 12.2 KM",
                            "payload": "ruta de los contabandistas",
                            "type": "postback"
                            },
                            {
                            "title": "Más información",
                            "payload": "ruta de los contabandistas",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de los principales senderos de la ciudad",attachment=new_carousel)
        return []
# atractivos sin costo
class ActionCarousel(Action):
    def name(self) -> Text:
        return "listalugares_sincosto"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Parque de la Familia Baños de Agua Santa",
                        "subtitle": "Ingreso: $0",
                        "image_url": "https://img.goraymi.com/2019/11/15/b66b31b294e57c0ede5bdbacd42884ab_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Parque+de+la+Familia+Ba%C3%B1os/@-1.3973445,-78.3816562,18z/data=!3m1!4b1!4m12!1m6!3m5!1s0x91d393e0df5e73a7:0x7ea2c1b415c3f560!2sParque+de+la+Familia+Ba%C3%B1os!8m2!3d-1.3973445!4d-78.3805619!3m4!1s0x91d393e0df5e73a7:0x7ea2c1b415c3f560!8m2!3d-1.3973445!4d-78.3805619?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "parque de la familia",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Santuario Nuestra Señora del Rosario de Agua Santa",
                        "subtitle": "Precio: $0",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/605242bb8e9617719570c243/f24ff980-43f9-420a-b3f3-94109de0e14e/Iglesia+de+Banos+Ecuador+-+Basilica+de+la+Virgen+de+Agua+Santa.jpeg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Santuario+y+Bas%C3%ADlica+Cat%C3%B3lica+Nuestra+Se%C3%B1ora+del+Rosario+de+Agua+Santa+de+Ba%C3%B1os/@-1.3974067,-78.4229707,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912257227d11:0xa2908f10209f3f74!8m2!3d-1.3974067!4d-78.420782?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "iglesia de baños",
                            "type": "postback"
                            }
                        ]
                    }
                    # ,
                    # {
                    #     "title": "Mirador Ojos del Volcán",
                    #     "subtitle": "Precio: $0",
                    #     "image_url": "https://img.goraymi.com/2018/09/20/4bb1a2d914e2adb025deb2c064e614b2_xl.jpg",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Cómo llegar",
                    #         "url": "https://www.google.com.ec/maps/place/1%C2%B023'03.5%22S+78%C2%B026'13.2%22W/@-1.384301,-78.4375342,19z/data=!3m1!4b1!4m6!3m5!1s0x0:0x91fae3b0333f36be!7e2!8m2!3d-1.3843008!4d-78.4369872?hl=es",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "más información ojos del volcan ",
                    #         "type": "postback"
                    #         }
                    #     ]
                    # }
                    ,
                    {
                        "title": "Balneario  Zuñag",
                        "subtitle": "Precio: $0",
                        "image_url": "https://docplayer.es/docs-images/68/58662593/images/51-1.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Riverside+Eco+Resort/@-1.407416,-78.192198,1555m/data=!3m1!1e3!4m8!3m7!1s0x0:0xea9332f8a65e1244!5m2!4m1!1i2!8m2!3d-1.408801!4d-78.192779?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "balneario Zuñag",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Malecón Rio Verde",
                        "subtitle": "Precio: $0",
                        "image_url": "https://www.eluniverso.com/resizer/Ys1FwVC7b3VqzdTQsZpQLeckuys=/1435x670/smart/filters:quality(70)/cloudfront-us-east-1.images.arcpublishing.com/eluniverso/CKHAHQVMVJHBXEADYI6RKQR22Q.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/R%C3%ADo+Verde/@-1.4031057,-78.3005047,18z/data=!3m1!4b1!4m6!3m5!1s0x91d3934e3e855e95:0x983621474f652d95!8m2!3d-1.40344!4d-78.3009985!16s%2Fg%2F1tfpwbl7?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "malecon rio verde",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de lugares sin costo para visitar",attachment=new_carousel)
        return []
# fin atractivos sin costo 
# nuevos atractivos
class ActionCarousel(Action):
    def name(self) -> Text:
        return "nuevos_atractivos"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "La Torre Shaya",
                        "subtitle": "Ingreso: $0",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipPCZnHHfQyeif77y7wK2vnUBmSEI2bsEAse1GmQ=s680-w680-h510",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/dir//-1.3994935,-78.4196495/@-1.3996163,-78.4200011,19.73z/data=!4m2!4m1!3e0",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "Torre Shaya",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Sacha 360º Mirador & Café",
                        "subtitle": "Precio: $2",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipP-GGFUDcPJbOtidJP0ONQmwPDMQc2cBZTjZ3EJ=s680-w680-h510",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Mirador+Bellavista/@-1.4000673,-78.4141538,17.74z/data=!4m5!3m4!1s0x91d3913c1d36eb8b:0x2c9e1347581728e7!8m2!3d-1.3998779!4d-78.4145889?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "información de Sacha 360 ",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/sacha.360",
                            "type": "web_url"
                            }
                        ]
                    }
                    # ,
                    # {
                    #     "title": "Sendero Piedra de la Luz",
                    #     "subtitle": "Precio: $0",
                    #     "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t1.6435-9/104109618_2072162669594687_7823747376366681190_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeGgLO453TYXXPmChz_sgO_uCdWdF87wZI4J1Z0XzvBkjmJlYN-RO6ik81VznEVCkbcO6pofkeJ-K8Ln1Honi-bT&_nc_ohc=vH_3K-665N8AX9C-50i&_nc_ht=scontent.fatf4-1.fna&oh=00_AfDYpi-cxM9keHfZryKhhoU5hCiz3HNftzQ4BWdn2zB8eA&oe=63C627A8",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Cómo llegar",
                    #         "url": "",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "piedra de a luz",
                    #         "type": "postback"
                    #         }
                    #     ]
                    # },
                    # {
                    #     "title": "Sendero Cara de Perro",
                    #     "subtitle": "Precio: $0",
                    #     "image_url": "https://s2.wklcdn.com/image_135/4068881/34192343/22060520.jpg",
                    #     "buttons": [ 
                    #         {
                    #         "title": "Cómo llegar",
                    #         "url": "https://es.wikiloc.com/rutas-senderismo/cara-de-perro-ulba-banos-de-agua-santa-34192343",
                    #         "type": "web_url"
                    #         },
                    #         {
                    #         "title": "Más información",
                    #         "payload": "cara de perro",
                    #         "type": "postback"
                    #         }
                    #     ]
                    # }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de los nuevos atractivos de la cuidad",attachment=new_carousel)
        return []
# chivas
class ActionCarousel(Action):
    def name(self) -> Text:
        return "chivas"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Recorrido:",
                        "subtitle": "Precio: $2",
                        "image_url": "",
                        "buttons": [
                            {
                            "title": "Cómo llegar",
                            "url": "",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Recorrido:",
                        "subtitle": "Precio: $2",
                        "image_url": "",
                        "buttons": [
                            {
                            "title": "Cómo llegar",
                            "url": "",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "sacha cafe",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Recorrido:",
                        "subtitle": "Precio: $0",
                        "image_url": "",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/TERMINAL+TUR%C3%8DSTICO+DE+CHIVAS/@-1.3959865,-78.4250798,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39138623b5fcb:0x25ec44f1a46c2efb!8m2!3d-1.3959865!4d-78.4228858",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piedra de a luz",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Recorrido:",
                        "subtitle": "Precio: $2",
                        "image_url": "",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/TERMINAL+TUR%C3%8DSTICO+DE+CHIVAS/@-1.3959865,-78.4250798,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39138623b5fcb:0x25ec44f1a46c2efb!8m2!3d-1.3959865!4d-78.4228858",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "cara de perro",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de recorridos de chivas",attachment=new_carousel)
        return []
# centro de la ciudad
class ActionCarousel(Action):
    def name(self) -> Text:
        return "centro_list"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Cascada de la Virgen",
                        "subtitle": "Precio: $0",
                        "image_url": "https://c8.alamy.com/comp/2DR01F2/shrine-of-the-holy-mary-virgen-del-rosario-de-agua-santa-at-the-waterfall-cascada-manto-de-la-novia-banos-de-agua-santa-tungurahua-province-2DR01F2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Cascada+de+la+Virgen/@-1.3991067,-78.4196862,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3913cba4fe99f:0x9098e08ddb2d3d9f!8m2!3d-1.3991067!4d-78.4174975?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "cascada de la virgen",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Salto de puente",
                        "subtitle": "Precio: $20 por persona",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5d23b57617786c0001fcbeda/1572634731708-3FHOE9ODR6AJCFPVQ213/Salto-del-puente---puenting---San-Francisco---Banos.jpg",
                        "buttons": [
                            {
                            "title": "Más información",
                            "payload": "salto de puente",
                            "type": "postback"
                            },
                            {
                            "title": "Dónde contratar actividad",
                            "payload": "contratar salto de puente",
                            "type": "postback"
                            },
                            {
                            "title": "Precio",
                            "payload": "precio salto de puente ",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "La fábrica de chocolate en Baños",
                        "subtitle": "Precio: $0",
                        "image_url": "https://trafficamerican.com/wp-content/uploads/2022/06/fabrica-de-chocolate-3-1024x576.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/F%C3%A1brica+M%C3%A1gica+de+Chocolate/@-1.4009024,-78.4227217,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3910a2606524f:0x3db57affb6a3d064!8m2!3d-1.4009024!4d-78.4227217?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "frabrica de chocolate",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/FabricaMagicadeChocolate",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Cavernas Sigsi Huayco",
                        "subtitle": "Precio: $3",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_39768.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Caverna+Sigsi+-+Huayco/@-1.3943394,-78.421789,17z/data=!4m5!3m4!1s0x91d39165212546c9:0x42e1a13b977e0b55!8m2!3d-1.3943391!4d-78.4217909?hl=es-EC",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "cavernas Sigsi Huayco",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/cavernasigsihuayco/?show_switched_toast=0&show_invite_to_follow=0&show_switched_tooltip=0&show_podcast_settings=0&show_community_transition=0&show_community_review_changes=0&show_community_rollback=0&show_follower_visibility_disclosure=0",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Troll Mountain cine al aire libre",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://casasholidayhomes.com/images/blog_turismo/troll/troll.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/Troll+Mountain/@-1.3927375,-78.4246551,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912503a0a119:0x8ef81b133fb67ac2!8m2!3d-1.3927375!4d-78.4246551",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "troll mountain",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/trollmountain.ec/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "La Aldea Mágica",
                        "subtitle": "Precio: $3 adultos y $1,5 niños",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-o/15/50/31/1d/duende-de-arbol.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/place/La+Aldea+M%C3%A1gica/@-1.3922608,-78.4172929,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391bfa7b2cd93:0xb6f725d561390841!8m2!3d-1.3922608!4d-78.4172929",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "aldea magica",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/LaAldeaMagicaPAGINAOFICIAL/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "El bosque encantado",
                        "subtitle": "Precio: $4 adultos, $2 niños",
                        "image_url": "https://trafficamerican.com/wp-content/uploads/2022/07/ATRACCION-2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/El+Bosque+Encantado/@-1.4018859,-78.4253846,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912542817999:0x210785788b6a7fb6!8m2!3d-1.4018859!4d-78.4231906?hl=es&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "bosque encandado",
                            "type": "postback"
                            },
                            {
                            "title": "Redes sociales",
                            "url": "https://www.facebook.com/ElBosqueEncantadoEC/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "La Torre Shaya",
                        "subtitle": "Ingreso: $0",
                        "image_url": "https://thumbs.dreamstime.com/b/torre-en-banos-ecuador-110690957.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com/maps/dir//-1.3994935,-78.4196495/@-1.3996163,-78.4200011,19.73z/data=!4m2!4m1!3e0",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "Torre Shaya",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Santuario Nuestra Señora del Rosario de Agua Santa",
                        "subtitle": "Precio: $0",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/605242bb8e9617719570c243/f24ff980-43f9-420a-b3f3-94109de0e14e/Iglesia+de+Banos+Ecuador+-+Basilica+de+la+Virgen+de+Agua+Santa.jpeg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Santuario+y+Bas%C3%ADlica+Cat%C3%B3lica+Nuestra+Se%C3%B1ora+del+Rosario+de+Agua+Santa+de+Ba%C3%B1os/@-1.3974067,-78.4229707,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912257227d11:0xa2908f10209f3f74!8m2!3d-1.3974067!4d-78.420782?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "iglesia de baños",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Piscinas de la Virgen",
                        "subtitle": "Precio: $4 adultos y $2 niños",
                        "image_url": "https://i.pinimg.com/originals/17/f2/c4/17f2c40b4f48b539cd9385f704443bed.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Termas+de+la+Virgen/@-1.3982652,-78.4202581,17z/data=!4m5!3m4!1s0x91d39122c52c61fd:0xfaa0f21baa970208!8m2!3d-1.3987719!4d-78.4175783?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas de la virgen",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Termas de la Virgen",
                        "subtitle": "Precio: $6 adultos y $3 niños",
                        "image_url": "https://img.goraymi.com/2018/11/15/e5bc0af5084578b889a30f0cf7e16896_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Piscinas+Termas+De+La+Virgen+-+Ba%C3%B1os+Ecuador/@-1.3982652,-78.4202581,17z/data=!4m5!3m4!1s0x0:0x4c067c5ae04d1cd4!8m2!3d-1.3981689!4d-78.4185118?hl=es&shorturl=1&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "termas de la virgen",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Lista de atractivos cerca del centro de la ciudad",attachment=new_carousel)
        return []
#-- ingles
class ActionCarousel(Action):
    def name(self) -> Text:
        return "waterfall_lis"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "El manto de la novia Waterfall",
                        "subtitle": "Canopy: $10, Tarabita:$3 to $5",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/1c/e8/e4/5f/caption.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Cascada+Manto+de+la+Novia/@-1.4038417,-78.3355075,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3935b9ecfb70b:0xc1dfa16ac3d791df!8m2!3d-1.4038417!4d-78.3355075?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "manto de la novia waterfall",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Agoyan Waterfall",
                        "subtitle": "Canopy: $10, Tarabita:$3 to $5",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/16/6c/9b/b7/cascada-de-agoyan-banos.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/1%C2%B023'56.7%22S+78%C2%B022'10.6%22W/@-1.3990833,-78.3696111,17z/data=!3m1!4b1!4m6!3m5!1s0x0:0xcca17d10913a164e!7e2!8m2!3d-1.3990876!4d-78.3696065?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "agoyan waterfall",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "El pailon del diablo Waterfall",
                        "subtitle": "Price: $2,50",
                        "image_url": "https://www.laflorestahotel.com/archivos/blogs/pailon-del-diablo-banos-ecuador.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Cascada+El+Pailon+(del+Diablo)/@-1.4044668,-78.297827,17z/data=!3m1!4b1!4m5!3m4!1s0x91d393fc6b20ad6d:0xbfc06a78c4bded53!8m2!3d-1.4044668!4d-78.297827",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "pailon del diablo waterfall",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "La virgen waterfall",
                        "subtitle": "Price: $0",
                        "image_url": "https://c8.alamy.com/comp/2DR01F2/shrine-of-the-holy-mary-virgen-del-rosario-de-agua-santa-at-the-waterfall-cascada-manto-de-la-novia-banos-de-agua-santa-tungurahua-province-2DR01F2.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Cascada+de+la+Virgen/@-1.3991067,-78.4196862,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3913cba4fe99f:0x9098e08ddb2d3d9f!8m2!3d-1.3991067!4d-78.4174975?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "La virgen waterfall",
                            "type": "postback"
                            }
                        ]
                    }, 
                    {
                        "title": "Cascada Inés María",
                        "subtitle": "Price: $0",
                        "image_url": "https://s2.wklcdn.com/image_125/3750282/23303233/14787740.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Cascada+In%C3%A9s+Mar%C3%ADa+Ba%C3%B1os+Tungurahua/@-1.3957613,-78.4359408,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391f086f24d7b:0x9276d5515be8279!8m2!3d-1.3957613!4d-78.4359408?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "ines maria waterfall",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Cascada San Antonio",
                        "subtitle": "Price: $0",
                        "image_url": "http://www.southamericanpostcard.com/images/photos/ecuador-FABU3823_trip7.JPG",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Cascada+del+Silencio/@-1.4004158,-78.4006583,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3914274759349:0x6bbf01636ad0542e!8m2!3d-1.4004158!4d-78.4006583?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "san antonio waterfall",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Cascada de Chamana",
                        "subtitle": "Price: $0",
                        "image_url": "https://static.wixstatic.com/media/47d72f_d1ca7f265b0c4669a82797be9ddc9b5a~mv2_d_3024_3780_s_4_2.jpg/v1/fill/w_740,h_925,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/47d72f_d1ca7f265b0c4669a82797be9ddc9b5a~mv2_d_3024_3780_s_4_2.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Las+cascadas+de+chamana+y+ulbilla/@-1.4011036,-78.4101904,15z/data=!4m10!1m2!2m1!1sCascada+de+Chamana!3m6!1s0x91d3910b102e7401:0x839bf12cd93ca9e6!8m2!3d-1.4012667!4d-78.4002409!15sChJDYXNjYWRhIGRlIENoYW1hbmGSAQtoaWtpbmdfYXJlYeABAA!16s%2Fg%2F11k3rrpz01?hl=es-419",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "chamana waterfall",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="List of the main waterfalls in town",attachment=new_carousel)
        return []
# #---------------------------------------------------

# # #------------------------------------------
class ActionCarousel(Action):
    def name(self) -> Text:
        return "thematic_parks_list"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "The enchanted forest",
                        "subtitle": "Price: 4$ adults, 2$ children",
                        "image_url": "https://trafficamerican.com/wp-content/uploads/2022/07/ATRACCION-2.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/El+Bosque+Encantado/@-1.4018859,-78.4253846,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912542817999:0x210785788b6a7fb6!8m2!3d-1.4018859!4d-78.4231906?hl=es&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "enchanted forest",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/ElBosqueEncantadoEC/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Animal Park",
                        "subtitle": "Price: $6 adults, $3 children",
                        "image_url": "https://animalpark.ec/wp-content/uploads/2021/04/slide-2.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/ANIMALPARK+PARQUE+TEM%C3%81TICO/@-1.4101985,-78.415867,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3916adbe54ee5:0x2f996013fff3d1a!8m2!3d-1.4101985!4d-78.415867",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "animal park information",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/AnimalPark-1033209876818756/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Discovery Baños",
                        "subtitle": "Price: de $1 a $5",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-o/08/9f/ad/bb/discovery-banos.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Discovery+Ba%C3%B1os/@-1.3990065,-78.3801008,15z/data=!4m5!3m4!1s0x91d3936f1357ab43:0x853303c8b1a8dcdd!8m2!3d-1.398129!4d-78.3671952",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "discovery baños information",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/discoverybanos",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "San Martin adventure park ",
                        "subtitle": "Price: $20 por persona",
                        "image_url": "https://img.goraymi.com/2019/11/18/4c72d92de5c7f8c4a1d2961c442c59df_lg.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/PARQUE+AVENTURA+SAN+MARTIN/@-1.3949785,-78.4380035,17z/data=!3m1!4b1!4m5!3m4!1s0x91d390e7923fe599:0xcff71819fb57a886!8m2!3d-1.3949785!4d-78.4380035",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "san martin adventure park",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100083143339774",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Dinosaur Park",
                        "subtitle": "Price: $6 adults y $3,50 children",
                        "image_url": "https://directorio593.com/custom/domain_1/image_files/1080_photo_29926.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Dinosaurios+Park/@-1.4007348,-78.4105307,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3916d35e154f9:0x6c309bd68abe918d!8m2!3d-1.4007348!4d-78.4105307",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "dinosaur park",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/DinosauriosPark",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Our Mundo Adventure",
                        "subtitle": "Price: $3",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t39.30808-6/287528743_3068283230153316_7006248754419818901_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHjAUZX5XiMq_GnpqKTvfWCkiz_9vdYKYKSLP_291gpgjWgqJeKcRfn8PO8X7AKUkc7k99BeKoIO9ziCkgNNFCN&_nc_ohc=nFj4f8z4auMAX8rqm6y&_nc_ht=scontent.fatf4-1.fna&oh=00_AfC5m87ou135clc58hFtAflI2qen2PELBbZ2SD_zUEaTxw&oe=63ADE45B",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Dinosaurios+Park/@-1.4007348,-78.4105307,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3916d35e154f9:0x6c309bd68abe918d!8m2!3d-1.4007348!4d-78.4105307",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "our mundo adventure",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/PueblodelMundo",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "PiQchur photo park",
                        "subtitle": "Price: $3 adults y $2 children",
                        "image_url": "https://directorio593.com/custom/domain_1/image_files/sitemgr_photo_35746.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/piQchur/@-1.3808585,-78.4309264,15.74z/data=!4m5!3m4!1s0x91d3916227fcf88f:0x931dfc6c796985c6!8m2!3d-1.379453!4d-78.4364488?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "piqchur photo park",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/piqchuroficial/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "The Magic Village",
                        "subtitle": "Price: $3 adults y $1,5 children",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-o/15/50/31/1d/duende-de-arbol.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/La+Aldea+M%C3%A1gica/@-1.3922608,-78.4172929,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391bfa7b2cd93:0xb6f725d561390841!8m2!3d-1.3922608!4d-78.4172929",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "the magic village",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/LaAldeaMagicaPAGINAOFICIAL/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Troll Mountain outdoor cinema",
                        "subtitle": "Price: $2 adults y $1 children",
                        "image_url": "https://casasholidayhomes.com/images/blog_turismo/troll/troll.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Troll+Mountain/@-1.3927375,-78.4246551,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912503a0a119:0x8ef81b133fb67ac2!8m2!3d-1.3927375!4d-78.4246551",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "more about Troll mountain",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/trollmountain.ec/",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Sigsi Huayco Caverns",
                        "subtitle": "Price: $3",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_39768.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Caverna+Sigsi+-+Huayco/@-1.3943394,-78.421789,17z/data=!4m5!3m4!1s0x91d39165212546c9:0x42e1a13b977e0b55!8m2!3d-1.3943391!4d-78.4217909?hl=es-EC",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "Sigsi Huayco Caverns",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/cavernasigsihuayco/?show_switched_toast=0&show_invite_to_follow=0&show_switched_tooltip=0&show_podcast_settings=0&show_community_transition=0&show_community_review_changes=0&show_community_rollback=0&show_follower_visibility_disclosure=0",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Theme Parks List",attachment=new_carousel)
        return []
# # miradores en ingles 
# #---------------------------------------------------
class ActionCarousel(Action):
    def name(self) -> Text:
        return "viewpoints_ingles"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "The Feet of God",
                        "subtitle": "Price: $2",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t39.30808-6/281362098_156223570268463_3917025565137347655_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=a26aad&_nc_eui2=AeGZet7D-vEelFU4AyAj6lItzi2i-NNJGYbOLaL400kZhgE2kwsPhGNDqZ4kevRXlm_o6C7dbUOkikvMkMONPSnl&_nc_ohc=NJiIUFELRKkAX-4Ywn1&_nc_ht=scontent.fatf4-1.fna&oh=00_AfCSskVjIQ9wb9zPioIE0nICWBBkpDlI8CtFlNqrZJtkiA&oe=63A37E74",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Mirador+Los+Pies+de+Dios/@-1.3801102,-78.4362743,18z/data=!4m5!3m4!1s0x91d391879e7356d7:0x3db0a0abbdc09796!8m2!3d-1.3797852!4d-78.4358587",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "the feet of god",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/lospiesdedios",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Sacha 360º Mirador & Café",
                        "subtitle": "Price: $2",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipP-GGFUDcPJbOtidJP0ONQmwPDMQc2cBZTjZ3EJ=s680-w680-h510",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Mirador+Bellavista/@-1.4000673,-78.4141538,17.74z/data=!4m5!3m4!1s0x91d3913c1d36eb8b:0x2c9e1347581728e7!8m2!3d-1.3998779!4d-78.4145889?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "Sacha Viewpoint ",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/sacha.360",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Bellavista Viewpoint",
                        "subtitle": "Price: 50 centns",
                        "image_url": "https://www.georges-backpackingguides.com/wp-content/uploads/2022/06/Mirador.Banos_.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Mirador+Bellavista/@-1.4000673,-78.4141538,17.74z/data=!4m5!3m4!1s0x91d3913c1d36eb8b:0x2c9e1347581728e7!8m2!3d-1.3998779!4d-78.4145889?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "Bellavista viewpoint",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Revolving cafeteria in Baños",
                        "subtitle": "Price: $3 ",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/1c/bb/3c/3e/20210225-105848-largejpg.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Caf%C3%A9+Giratorio/@-1.3974038,-78.4170547,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391aae1cbe637:0x217849fcd907495d!8m2!3d-1.3974038!4d-78.4148607?hl=es&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "revolving cafe",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100083339372432",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "The kiss of the moon",
                        "subtitle": "Price: $1",
                        "image_url": "https://www.imagineecuador.com/wp-content/uploads/2021/10/Recurso-93-8.png",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/El+Beso+de+la+Luna/@-1.3788181,-78.4392336,17z/data=!4m5!3m4!1s0x91d391e38590ac21:0xb4f3a3c3f315ba41!8m2!3d-1.3788181!4d-78.4370449?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "moon kiss",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100076001416193",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "The Eagle's Nest | Volcano Eyes",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://lh3.googleusercontent.com/p/AF1QipNsJpRk-xpUaLKWixLSzuMjXajnoKupBJpyHMYQ=w960-h960-n-o-v1",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Mirador+ojos+del+volcan-nido+del+%C3%A1guila/@-1.3841049,-78.4375218,20z/data=!4m5!3m4!1s0x91d391beeaec81b5:0xa4dc9d7b99120599!8m2!3d-1.3839639!4d-78.4375822",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "volcano eyes",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/refugioojosdelvolcan",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "El Ventanal de Kong",
                        "subtitle": "Price: $2",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_41480.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/El+Ventanal+de+Kong/@-1.3838545,-78.4369699,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391870480f17f:0x81915689d7b2ce1f!8m2!3d-1.3838545!4d-78.4369699?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "information about the ventanal de kong",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100075968306264",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Christ the Redeemer",
                        "subtitle": "Price: $2",
                        "image_url": "https://www.turismoecuador24.com/archivos/destinos/cristo_redentor-turismo_ecuador_24.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Cristo+Redentor+de+Ba%C3%B1os+de+Agua+Santa/@-1.3829375,-78.4360625,17z/data=!4m5!3m4!1s0x91d3917bd42d0fcd:0x778f7ccec5dde38c!8m2!3d-1.3829375!4d-78.4360625",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "Christ Redeemer",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100078904175317",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="List of the city's viewpoints",attachment=new_carousel)
        return []
# #------- bridges
class ActionCarousel(Action):
    def name(self) -> Text:
        return "bridges_sites"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "God's Hands",
                        "subtitle": "Price: Adults $2, children $1",
                        "image_url": "https://images.hive.blog/DQmQ2Gy7vYpNWFZMteM3EaPDyLjgdC5i3cFTWoWtTGMK7Xv/image.png",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/%22Las+Manos+de+Dios%22+Ba%C3%B1os+de+Agua+Santa/@-1.3786488,-78.4348441,17z/data=!4m5!3m4!1s0x91d391a051945545:0x1e2d2fbc28f64501!8m2!3d-1.378141!4d-78.4353729?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "hands of god",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100063900711510",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Pachamama's hand",
                        "subtitle": "Price: 5 $ adults and 2.50 $ children",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5a2eff3112abd936197728c6/1626387639488-Z6SS8CMI39JUMF04SPWF/La+Mano+de+la+Pachamama+-+El+Vuelo+del+Condor+-+Banos+Ecuador.jpeg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/LA+MANO+DE+LA+PACHAMAMA/@-1.4119061,-78.4166448,17z/data=!4m5!3m4!1s0x91d3918bcddb68d1:0x6dc3f85d8e127eae!8m2!3d-1.4136115!4d-78.414352?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "pachamama hands",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/elvuelodelcondorEC",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Glass bridge in Baños",
                        "subtitle": "Price: 7 dollars",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_35280.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Mega+Adventure+Park+R%C3%ADo+Blanco/@-1.3993073,-78.3489977,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39354abb33077:0xf040e636e8fffc47!8m2!3d-1.3993073!4d-78.3489977",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "crystal bridge",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/megaparkrioblanco",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "The Feet of God",
                        "subtitle": "Price: $2",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t39.30808-6/281362098_156223570268463_3917025565137347655_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=a26aad&_nc_eui2=AeGZet7D-vEelFU4AyAj6lItzi2i-NNJGYbOLaL400kZhgE2kwsPhGNDqZ4kevRXlm_o6C7dbUOkikvMkMONPSnl&_nc_ohc=NJiIUFELRKkAX-4Ywn1&_nc_ht=scontent.fatf4-1.fna&oh=00_AfCSskVjIQ9wb9zPioIE0nICWBBkpDlI8CtFlNqrZJtkiA&oe=63A37E74",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Mirador+Los+Pies+de+Dios/@-1.3801102,-78.4362743,18z/data=!4m5!3m4!1s0x91d391879e7356d7:0x3db0a0abbdc09796!8m2!3d-1.3797852!4d-78.4358587",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "the Feet of God",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/lospiesdedios",
                            "type": "web_url"
                            }
                        ]
                    },
                ]
                }
        }
        dispatcher.utter_message(text="List of attractions",attachment=new_carousel)
        return []
# #------ free
class ActionCarousel(Action):
    def name(self) -> Text:
        return "free_list"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Baños Family Park",
                        "subtitle": "Price: $0",
                        "image_url": "https://img.goraymi.com/2019/11/15/b66b31b294e57c0ede5bdbacd42884ab_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Parque+de+la+Familia+Ba%C3%B1os/@-1.3973445,-78.3816562,18z/data=!3m1!4b1!4m12!1m6!3m5!1s0x91d393e0df5e73a7:0x7ea2c1b415c3f560!2sParque+de+la+Familia+Ba%C3%B1os!8m2!3d-1.3973445!4d-78.3805619!3m4!1s0x91d393e0df5e73a7:0x7ea2c1b415c3f560!8m2!3d-1.3973445!4d-78.3805619?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "family park",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Church of Baños de Agua Santa",
                        "subtitle": "Precio: $0",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/605242bb8e9617719570c243/f24ff980-43f9-420a-b3f3-94109de0e14e/Iglesia+de+Banos+Ecuador+-+Basilica+de+la+Virgen+de+Agua+Santa.jpeg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Santuario+y+Bas%C3%ADlica+Cat%C3%B3lica+Nuestra+Se%C3%B1ora+del+Rosario+de+Agua+Santa+de+Ba%C3%B1os/@-1.3974067,-78.4229707,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3912257227d11:0xa2908f10209f3f74!8m2!3d-1.3974067!4d-78.420782?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "church of baños",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Malecón Rio Verde",
                        "subtitle": "Precio: $0",
                        "image_url": "https://www.eluniverso.com/resizer/Ys1FwVC7b3VqzdTQsZpQLeckuys=/1435x670/smart/filters:quality(70)/cloudfront-us-east-1.images.arcpublishing.com/eluniverso/CKHAHQVMVJHBXEADYI6RKQR22Q.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/R%C3%ADo+Verde/@-1.4031057,-78.3005047,18z/data=!3m1!4b1!4m6!3m5!1s0x91d3934e3e855e95:0x983621474f652d95!8m2!3d-1.40344!4d-78.3009985!16s%2Fg%2F1tfpwbl7?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "malecon de rio verde information",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Free sites",attachment=new_carousel)
        return []
# #--- zoo
class ActionCarousel(Action):
    def name(self) -> Text:
        return "zoo_englis"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Vida Exotica Zoo",
                        "subtitle": "Price: $3 adults, $2 children",
                        "image_url": "https://www.directorio593.com/custom/domain_1/image_files/sitemgr_photo_31318.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Zoo+Vida+Ex%C3%B3tica/@-1.3964769,-78.4371854,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39132e15856eb:0x3d22b5c776b39ea5!8m2!3d-1.3964769!4d-78.4371854?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "The zoo vida exotica",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/zoovidaexotika",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "San Martin Zoo",
                        "subtitle": "Price: $4 adults, $3 children",
                        "image_url": "http://ecozoosanmartin.com/wp-content/uploads/2013/06/OsodeAnteojosZooEcuador-800x400.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Eco+zool%C3%B3gico+San+Mart%C3%ADn/@-1.396424,-78.4368971,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39169fd59315f:0xd51a7cbb561db913!8m2!3d-1.396424!4d-78.4368971",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "San Martin Zoo",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/ecozoologicosanmartinecuador",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Zoos of Baños de Agua Santa",attachment=new_carousel)
        return []
# #----museum
class ActionCarousel(Action):
    def name(self) -> Text:
        return "museum_banios"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Fray Enrique Mideros Museum",
                        "subtitle": "Price: $2 adults and $1 children",
                        "image_url": "https://img.goraymi.com/2018/06/15/50d5c37f048b430a3c3c78a98c8cbd68_lg.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Museo+Fray+Enrique+Mideros/@-1.3973952,-78.4210431,17z/data=!3m1!4b1!4m5!3m4!1s0x91d39122fe8dffd5:0xafb55ec348545273!8m2!3d-1.3973952!4d-78.4210431?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "Fray Enrique Mideros museum",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100064109942493",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Museums of Baños de Agua Santa",attachment=new_carousel)
        return []
# #----gastronomy
class ActionCarousel(Action):
    def name(self) -> Text:
        return "gastronomy_sites"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Chocolate Factory",
                        "subtitle": "Price: $0",
                        "image_url": "https://trafficamerican.com/wp-content/uploads/2022/06/fabrica-de-chocolate-3-1024x576.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/F%C3%A1brica+M%C3%A1gica+de+Chocolate/@-1.4009024,-78.4227217,17z/data=!3m1!4b1!4m5!3m4!1s0x91d3910a2606524f:0x3db57affb6a3d064!8m2!3d-1.4009024!4d-78.4227217?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "chocolate factory",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/FabricaMagicadeChocolate",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="Gastronomic attractions",attachment=new_carousel)
        return []
#-- extrem activities
class ActionCarousel(Action):
    def name(self) -> Text:
        return "extreme_activities"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Rafting",
                        "subtitle": "Price: $ 30",
                        "image_url": "https://samarispa.com/wp-content/uploads/2021/05/WhatsApp-Image-2021-06-03-at-9.12.52-AM-1024x576.jpeg",
                        "buttons": [ 
                            {
                            "title": "About",
                            "payload": "rafting activity",
                            "type": "postback"
                            },
                            {
                            "title": "hire",
                            "payload": "i want to hire rafting",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Canyoning",
                        "subtitle": "Price: $ 30",
                        "image_url": "http://banosecuador.com/wp-content/uploads/2011/12/Team-Adventure-Canyoning.jpg",
                        "buttons": [
                            {
                            "title": "About",
                            "payload": "extreme activity canyoning",
                            "type": "postback"
                            },
                            {
                            "title": "hire",
                            "payload": "I want to hire canyoning",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Rock Climbing",
                        "subtitle": "Precio: $30 por persona",
                        "image_url": "https://www.imagineecuador.com/wp-content/uploads/2021/11/Recurso-114-e1637340114259.png",
                        "buttons": [
                            {
                            "title": "About",
                            "payload": "rock climbing",
                            "type": "postback"
                            },
                            {
                            "title": "hire",
                            "payload": "i want to contract rock climbing",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Bridge Jumping",
                        "subtitle": "Precio: $20 por persona",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5d23b57617786c0001fcbeda/1572634731708-3FHOE9ODR6AJCFPVQ213/Salto-del-puente---puenting---San-Francisco---Banos.jpg",
                        "buttons": [
                            {
                            "title": "About",
                            "payload": "bridge jumping",
                            "type": "postback"
                            },
                            {
                            "title": "hire",
                            "payload": "i want to hire bridge jumping",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="extreme activities:",attachment=new_carousel)
        return []
# #--- swings
class ActionCarousel(Action):
    def name(self) -> Text:
        return "swings_ingles_lis"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Fantasies of Flying Swing",
                        "subtitle": "Price: $  10 ",
                        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/12/3a/ef/5d/volando-sobre-banos-de.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/Columpio+Fantasias+De+Volar/@-1.408059,-78.424434,15z/data=!4m5!3m4!1s0x91d391293662b1f9:0x8e02011f4a7c3c24!8m2!3d-1.408059!4d-78.424434?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "fantasies of flying",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/profile.php?id=100047005794637",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Treehouse",
                        "subtitle": "Price: from $1 to $2",
                        "image_url": "https://i.pinimg.com/originals/09/44/c8/0944c8a8a067ebb71458e2b8626339b7.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/La+Casa+del+Arbol/@-1.4182111,-78.4263339,17z/data=!3m1!4b1!4m5!3m4!1s0x91d396d429a823e3:0x88718e7ae34cd3a5!8m2!3d-1.4182111!4d-78.4263339?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "tree house",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/lacasadelarbolec",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "El Vuelo del Cóndor",
                        "subtitle": "Price: $10",
                        "image_url": "https://goecuador.net/archivos/minegocio/el-vuelo-del-condor-banos-de-agua-santa-ecuador_2.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com.ec/maps/place/LA+MANO+DE+LA+PACHAMAMA/@-1.4119061,-78.4166448,17z/data=!4m5!3m4!1s0x91d3918bcddb68d1:0x6dc3f85d8e127eae!8m2!3d-1.4136115!4d-78.414352?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "vuelo del condor swing",
                            "type": "postback"
                            },
                            {
                            "title": "Social networks",
                            "url": "https://www.facebook.com/elvuelodelcondorEC",
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="List of swings",attachment=new_carousel)
        return []
#---trails
class ActionCarousel(Action):
    def name(self) -> Text:
        return "caminatas_ciudad"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Bellavista trail",
                        "subtitle": "Price: $0,50",
                        "image_url": "https://th.bing.com/th/id/R.bcb30384c27819ec4f3708d362e9223d?rik=j3D3V0r3oDp%2bhA&riu=http%3a%2f%2f1.bp.blogspot.com%2f-sLkfaGJhvg8%2fU1RZgRbQdDI%2fAAAAAAAACcs%2f46T7AzGA8ro%2fs1600%2fDSC_0408_EatPrayCureTravel.JPG&ehk=gdM3eLaWN%2fK7XE%2fkQvyyyeG4TNN5eEoj9%2b8us6YRSis%3d&risl=&pid=ImgRaw&r=0",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/mirador-la-cruz-bellavista?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 2.7 KM",
                            "payload": "Bellavista trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "Bellavista trail",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "The Sauces trail",
                        "subtitle": "Price: $ 0",
                        "image_url": "https://s2.wklcdn.com/image_120/3605816/55576940/37153943.700x525.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/sendero-de-los-sauces?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 6.8 KM",
                            "payload": "sauces trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "sauces trail",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "La virgen trail",
                        "subtitle": "Price: $0",
                        "image_url": "https://c8.alamy.com/compes/f52n4d/banos-canton-es-un-canton-de-ecuador-ubicada-en-la-provincia-de-tungurahua-vista-desde-el-mirador-de-la-virgen-f52n4d.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/monumento-a-la-virgen-de-banos?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 1.3 KM",
                            "payload": "la virgen trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "la virgen trail",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Pondoa trail",
                        "subtitle": "Precio: $ 0",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t1.6435-9/196548864_2130913640540454_2609577053806143772_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeEyeczG7tA_cAhCLeMu8ZK8GO7g8uZozgcY7uDy5mjOBykjh_n8Xshudnogdw1PR-d0XFVFxCh7q6lGUV_5NaRz&_nc_ohc=9G8EPfKfBEcAX-A35RI&_nc_ht=scontent.fatf4-1.fna&oh=00_AfDgZ3rf9j7pg8DiK2fzeF1ehW7TolgQhE07Hd0Ge-Ppxg&oe=63C0E286",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.google.com/maps/place/Sendero+a+Pondoa/@-1.4007698,-78.4364347,17z/data=!3m1!4b1!4m5!3m4!1s0x91d391d6436e7e6f:0x1c32fa521ad578f!8m2!3d-1.4007752!4d-78.434246",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 2.8 KM",
                            "payload": "pondoa trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "pondoa trail",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Luna Volcan trail",
                        "subtitle": "Precio: $0",
                        "image_url": "https://s2.wklcdn.com/image_106/3201816/31932374/20536574Master.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://es.wikiloc.com/rutas-senderismo/banos-luna-volcan-mirador-de-la-virgen-banos-a-bajo-ritmo-81822619",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 5.9 KM",
                            "payload": "luna volcan trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "luna volcan trail",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Tree house trail",
                        "subtitle": "Precio: $0",
                        "image_url": "https://www.santacruzbackpackers.com/archivos/blogs/mirador-banos.jpg",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/torre-al-cielo-y-casa-del-arbol?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 6.3 KM",
                            "payload": "tree house trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "tree house trail",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Contrabandistas trail",
                        "subtitle": "Price: $0",
                        "image_url": "https://scontent.fatf4-1.fna.fbcdn.net/v/t1.6435-9/37737585_233076270667185_1514949331688357888_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_eui2=AeEWqZM7XUKKPDsBmJVdFYc9JVBCoqD0gD4lUEKioPSAPpsnXopNzYxj4redVQ5VZJdWRktURc4g1d6BqkoPQXEi&_nc_ohc=kNg6ypTInMsAX-IFRsL&_nc_ht=scontent.fatf4-1.fna&oh=00_AfCVYdF1TnHdzE4yeYE2NPI6xkMMXK-UDsLv4QSDVA5RLg&oe=63C0EEA4",
                        "buttons": [ 
                            {
                            "title": "Get directions",
                            "url": "https://www.alltrails.com/es/explore/trail/ecuador/tungurahua/sendero-de-los-contrabandistas?mobileMap=false&ref=sidebar-static-map",
                            "type": "web_url"
                            },
                            {
                            "title": "Distance: 12.2 KM",
                            "payload": "contabandistas trail",
                            "type": "postback"
                            },
                            {
                            "title": "About",
                            "payload": "contabandistas trail",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="List of the main trails in the city",attachment=new_carousel)
        return []
#------swimming pools 
class ActionCarousel(Action):
    def name(self) -> Text:
        return "swimming_pool"
    
    def run(self, dispatcher:CollectingDispatcher, 
            tracker: Tracker, 
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        new_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "La Virgen Swimming Pool",
                        "subtitle": "Price: $4 adults and $2 children",
                        "image_url": "https://i.pinimg.com/originals/17/f2/c4/17f2c40b4f48b539cd9385f704443bed.jpg",
                        "buttons": [ 
                            {
                            "title": "Get informations",
                            "url": "https://www.google.com.ec/maps/place/Termas+de+la+Virgen/@-1.3982652,-78.4202581,17z/data=!4m5!3m4!1s0x91d39122c52c61fd:0xfaa0f21baa970208!8m2!3d-1.3987719!4d-78.4175783?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "swimming pools of la virgen",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Termas de la Virgen",
                        "subtitle": "Price: $6 adults and $3 children",
                        "image_url": "https://img.goraymi.com/2018/11/15/e5bc0af5084578b889a30f0cf7e16896_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Get informations",
                            "url": "https://www.google.com.ec/maps/place/Piscinas+Termas+De+La+Virgen+-+Ba%C3%B1os+Ecuador/@-1.3982652,-78.4202581,17z/data=!4m5!3m4!1s0x0:0x4c067c5ae04d1cd4!8m2!3d-1.3981689!4d-78.4185118?hl=es&shorturl=1&shorturl=1",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "termas de la virgen swimming pools",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Santa Clara Swimming Pool",
                        "subtitle": "Price: $4 adults and $2 children",
                        "image_url": "https://img.goraymi.com/2018/11/15/974392d06c3f723d04e88225e08b35c1_lg.jpg",
                        "buttons": [ 
                            {
                            "title": "Get informations",
                            "url": "https://www.google.com.ec/maps/place/Balneario+Santa+Clara+(El+Cangrejo)/@-1.3979118,-78.4213715,17z/data=!4m5!3m4!1s0x0:0x5103de56b1fb15b6!8m2!3d-1.4006486!4d-78.4193153?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "About",
                            "payload": "santa clara swimming pool",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "El Salado Thermal Pools",
                        "subtitle": "Precio: $3 adultos y $1,5 niños",
                        "image_url": "https://images.squarespace-cdn.com/content/v1/5d23b57617786c0001fcbeda/1572902830025-QDYPG9EQJPRM0XAJ5PS4/Termas%2BEl%2BSalado%2BBanos%2B2.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Balneario+El+Salado/@-1.402449,-78.436153,16z/data=!4m5!3m4!1s0x91d390d82c079589:0x3a89a5ac6ad94ee6!8m2!3d-1.4045738!4d-78.4323045?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas el salado ",
                            "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "Santa Ana Swimming Pool",
                        "subtitle": "Precio: $2 adultos y $1 niños",
                        "image_url": "https://img.goraymi.com/2018/11/15/d2de0f2f75de9f27db3d115f912eb2d1_xl.jpg",
                        "buttons": [ 
                            {
                            "title": "Cómo llegar",
                            "url": "https://www.google.com.ec/maps/place/Complejo+Santa+Ana/@-1.3955988,-78.4113088,17z/data=!4m5!3m4!1s0x91d3913fd7090945:0xa536512b9305557!8m2!3d-1.3953593!4d-78.4092785?hl=es",
                            "type": "web_url"
                            },
                            {
                            "title": "Más información",
                            "payload": "piscinas santa ana",
                            "type": "postback"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(text="List of the city's main swimming pools",attachment=new_carousel)
        return []