
# Declara los personajes usados en el juego como en el ejemplo:
define dec = Character('Detective', color="#93B5BB")
define decP = Character('Pensamientos', color="#62A18E")
define file = Character('Documento', color="#C29A54")
define desc = Character('???', color="#C4B0D7")
define off = Character('Oficial de Policia', color="3069F7")
image decImg = "Dect.png"
image stalImg = "Stalk.png"
image laptop = "Laptop.png"
image fondo = "Casa.jpg" # La imagen del frente de la casa de los suburbios
image pasillo = "Pasillo.jpg"
image despacho = "Despacho.jpeg"
image goodEnding = "Amanecer.jpeg"
image backyard = "backyard.jpeg"


# El juego comienza aquí.

label start:
    # Mostramos el texto de introducción
    play music ("audio/background.mp3")
    "Es 14 de Febrero de 20XX, dia de San Valentin."
    "Mientras las personas celebran, llega una llamada al departamento de Policia."
    "Una familia desaparece sin dejar rastro, y las evidencias apuntan a que se escaparon... ¿Pero de qué?."
    "Esta es la historia de un detective que se enfrenta a un caso que parece ser uno mas del monton, pero que esconde un oscuro secreto."
    "¿Podrá el detective resolver el caso y encontrar a la familia? ¿O será demasiado tarde?"
    "Tú decides."

    # Continuamos con el juego
    jump prologo
    #prologo
    label prologo:
    # Mostramos el texto del prólogo
    # Mostramos el fondo de la casa
    scene fondo with fade 
    show decImg at right
    dec "He sido Detective suficiente tiempo para saber que el dia de San Valentin es mas oscuro de lo que se cree."
    dec "Estoy llegando a una casa en la que se reportó una posible desaparición."
    dec "Según dicen en el reporte, quien llamó era vecina de la familia, que insinua que fue un secuestro, pero la situación es muy extraña."
    dec "¿Un secuestro en medio de un barrio suburbano en plena luz del día y en el Dia de San Valentin?"
    dec "Mis colegas sospechan que la familia se escapó para evadir su hipoteca, ya que al parecer tenían una deuda considerable." 
    dec "Pero mi instinto no se lo cree, los archivos indican que la familia no tenian verdaderos motivos para huir."
    dec "Quizas por eso me asignaron el caso."
    dec "¿Deberia entrar a la casa o investigar los alrededores?"
    hide decImg with dissolve
    # Mostramos el menú con las opciones de entrar o investigar 
    menu:
        "Entrar a la Casa.":
                jump stageone
                label stageone:
                    scene black with fade
                    "Cruzas el patio frontal, la puerta esta abierta."
                    "El equipo forense aún no llega, por lo que decides ponerte guantes."
                    scene pasillo with fade
                    "Todo esta completamente desordenado, pareciera que el lugar fue saqueado."
                    show decImg at right
                    dec "Jum."
                    dec "Es como si hubiesen tenido prisa de irse."
                    hide decImg with dissolve
                    decP "{b}¿Será que si se escaparon?{/b}"
                    menu:
                        "Mis colegas tienen razón, la deuda fue mayor a lo que podian pagar.":
                            jump badending
                            label badending:
                                scene black with fade
                                "Decidiste escuchar las opiniones de los demás antes que tu instinto."
                                "La Familia pagará el precio."
                                "The End."
                                return
                        "Seguiré investigando.":
                            jump stagetwo
                            label stagetwo:
                                scene black with fade
                                "Pasas más de una hora buscando pistas, todo sigue indicando a que escaparon."
                                scene pasillo with fade
                                show decImg at left
                                dec "Es impresionante, ni cuando es un caso de escape verdadero hay tantas evidencias." 
                                hide decImg with dissolve 
                                decP "{b}Tengo un mal presentimiento{/b}"
                                "Al final del pasillo hay una puerta que resalta, pero tiene seguro, no la logras abrir."
                                decP "Solo me falta esa habitación, siento que ahí tendré las respuestas que necesito."
                                decP "{b}¿Y si la derribo?{/b}"
                                show decImg at left
                                dec "Si estoy en lo correcto, conseguiré lo que necesito."
                                hide decImg with dissolve
                                decP "{b}Pero si me equivoco..."
                                show decImg at left
                                dec "Además de volverme la burla de la comisaria, recibiría mi tercer advertencia."
                                hide decImg with dissolve
                                menu:
                                    "No importa. El fin justifica los medios. (Recomiendo bajar volumen de efectos)":
                                        jump stagethree
                                        label stagethree:
                                            scene black with fade
                                            "Aviso del juego: Recomiendo bajar volumen de efectos."
                                            play sound("audio/sound.mp3")
                                            scene despacho with fade
                                            "No hizo falta mucha fuerza, lograste entrar a la oficina del hogar."
                                            "A diferencia del resto de la casa, todo esta ordenado y con un agradable olor."
                                            show decImg at right
                                            dec "Vaya, es un lindo despacho."
                                            hide decImg with dissolve
                                            decP "¿En esta habitación hay dos lunas?"
                                            show decImg at right
                                            dec "Empezaré a investigar."
                                            hide decImg with dissolve
                                            scene black with fade
                                            menu: 
                                                "Empezar a investigar el escritorio":
                                                    jump stagecuatro
                                                    label stagecuatro:
                                                        scene despacho with fade
                                                        "Es una mesa de madera, sobre ella hay una Laptop desbloqueada y con un archivo de texto reciente."
                                                        show decImg at right
                                                        dec "A ver si hay algo util aquí."
                                                        hide decImg with dissolve
                                                        show laptop at left
                                                        file "Espero que cuando encuentres este archivo no sea demasiado tarde."
                                                        file "Mi familia y yo hemos sidos secuestrados."
                                                        file "Desde hace años somos acosados por un exnovio de mi esposa, se ha vuelto loco."
                                                        file "He tratado de todo para proteger a mi familia, pero no ha sido suficiente, siempre nos encuentra."
                                                        file "Sospecho que hará algo esta noche."
                                                        file "Le dejé cartas a mi vecina para que cuando vuelva a su casa llame a la policia."
                                                        file "Esa persona es astuta, no sé de qué pueda ser capaz."
                                                        file "Por favor, encuentranos."
                                                        file "El nombre de esta persona e-"
                                                        hide laptop with dissolve
                                                        "El mensaje termina abruptamente, como si alguien lo estuviera borrando pero fue interrumpido en el proceso."
                                                        show decImg at right
                                                        dec "¡Lo sabía! Esto era más de lo que parece, pediré refuerzos."
                                                        hide decImg with dissolve
                                                        decP "Buscaré cuándo fue redactado el archivo, quizás así puedan hacer un radio de busqueda."
                                                        show laptop at left
                                                        file "Ultima Modificación: Hace 15 minutos."
                                                        hide laptop with dissolve
                                                        decP "{b}¡¿15 minutos?!"
                                                        show decImg at right
                                                        dec "Esto es imposible, llevo en la casa desde hace horas."
                                                        hide decImg with dissolve
                                                        scene black with fade
                                                        "Se va la luz en toda la casa."
                                                        desc "Debiste creerle a tus colegas."
                                                        play sound("audio/soundH.mp3")
                                                        "Varias horas más tarde."
                                                        scene fondo with fade
                                                        off "Aqui el oficial T-777, hemos encontrado al Detective, repito, encontramos al Detective."
                                                        off "Sí, bueno... El {b}cadaver{/b} del Detective."
                                                        off "Se encuentra en la misma casa que la familia abandonó mientras escapaba de sus deudas." 
                                                        off "Seguramente el Detective los encontró y no quisieron dejar cabos sueltos."
                                                        off "Es una lástima."
                                                        scene black with fade
                                                        "El Detective murió por un golpe en la cabeza."
                                                        "A la familia se le dió orden de captura por el homicidio."
                                                        "A los 3 meses encontraron al esposo {b}muerto{/b}"
                                                        "Los oficiales siguen sin encontrar el resto de la familia."
                                                        "El Verdadero Culpable de todo"
                                                        "{b} Sigue Libre. {/b}"
                                                        return
                                                "Investigar la habitación.":
                                                    jump stagefive
                                                    label stagefive:
                                                        scene despacho with fade
                                                        decP "Hay algo que me incomoda de este lugar."
                                                        "El Detective saca su linterna y empieza a alumbar la habitación."
                                                        desc "¡AÚN ESTÁS A TIEMPO DE IRTE!"
                                                        "El Detective saca su arma y la apunta junto a la linterna al origen del grito."
                                                        show decImg at right
                                                        show stalImg at left
                                                        desc "Oye, escuchame, escuchame, escuchame."
                                                        dec "¡Quieto! Identificate."
                                                        hide decImg with dissolve
                                                        desc "Soy el {b}verdadero{/b} esposo."
                                                        desc "¡Estás en lo que sería {b}MI{/b} casa!"
                                                        hide stalImg with dissolve
                                                        decP "No se parece en nada a las fotos que hay en toda la casa."
                                                        show stalImg at left
                                                        dec "Lo diré de nuevo, identificate."
                                                        hide decImg with dissolve
                                                        show stalImg at left
                                                        desc "{b}¡Estás en mi casa!{/b}"
                                                        desc "{b}¡Estás en mi casa!{/b}"
                                                        desc "yo fui quien se casó con ella."
                                                        desc "{b}¡YO ME CASE CON ELLA!{/b}"
                                                        desc "No ese imbecil."
                                                        hide stalImg with dissolve
                                                        decP "Es inestable, debo tener cuidado."
                                                        show decImg at right
                                                        dec "Escuchame, esta es la casa de XXXX, el verdadero espos-"
                                                        hide decImg
                                                        show stalImg at left
                                                        desc "{b}¡YO SOY SU ESPOSO!{/b}"
                                                        hide stalImg with dissolve
                                                        decP "Esto no llevará a nada."
                                                        show decImg at right
                                                        dec "¡Estás bajo arresto por obstaculizar una investigación en proceso!"
                                                        dec "{b}¡Y por gritarme!{/b}"
                                                        hide decImg with dissolve
                                                        scene black with fade
                                                        "Luego de arrestar al desconocido descubres que él secuestró a la familia."
                                                        "Resultó ser un acosador que lleva molestando a la familia desde hace años."
                                                        scene goodEnding with fade
                                                        "Luego de horas de interrogar al sujeto la policia logra ubicar a la familia."
                                                        "La encuentran en un almacen a 4km de ahí."
                                                        "El sujeto habia vuelto para borrar evidencias justo cuando lo encontraste."
                                                        "Era alguien peligroso e inestable, hiciste bien en actuar bajo tu instinto."
                                                        "Todos están a salvo, gracias a ti."
                                                        "Felicitaciones."
                                                        "Gracias por Jugar."
                                                        return
                                    
                                    "Decides no arriesgarte y esperar a que los técnicos abran la puerta.":
                                        jump fatalending
                                        label fatalending:
                                            scene black with fade
                                            "La policia tardó en llegar 40 minutos."
                                            "Solo lograron encontrar una laptop destruida junto a una foto del padre de la familia quemada."
                                            "La Familia sigue desaparecida."
                                            return
                                                        
                            
        "Investigar los alrededores":
            jump sidestageone
            label sidestageone:
                scene black with fade
                "Decides investigar los alrededores de la casa por si hay pistas."
                scene backyard with fade
                show decImg at right
                dec "Lo mejor será ver si hay algo interesante por acá."
                dec "Entre tantos arbustos quizás consiga algo."
                hide decImg with dissolve
                scene black with fade
                "Algo brillante llama tu atención, resulta ser una llave junto a una nota"
                "{b}Encuentranos"
                scene backyard with fade
                show decImg at right
                dec "Esto es peor de lo que pensaba."
                dec "Debo actuar rápido, aunque llame por apoyo tardarían demasiado en llegar."
                hide decImg with dissolve
                decP "Entraré a la casa, ahí puedo ver qué abre esta llave."
                scene black with fade
                "Entras a toda velocidad a la casa."
                "Te encuentras con un pasillo oscuro."
                "Ya que no ha llegado el forense, decides ponerte guantes."
                scene pasillo with fade
                show decImg at left
                dec "Con tantas puertas y lugares en esta casa, ¿Cómo encontraré lo que abre esta llave?"
                hide decImg dissolve
                menu:
                    "Te desesperas":
                        jump sidestagetwo
                        label sidestagetwo:
                            show decImg at left
                            dec "Esto será imposible, ni teniendo toda la noche lo lograré."
                            dec "Mejor informo por la radio sobre la situación y que hagan un radio de busqueda."
                            dec "Cuando lleguen más agentes podremos encontrar qué abre esto."
                            hide decImg with dissolve
                            scene black with fade
                            "La policia tardó en llegar 20 minutos."
                            "Solo lograron encontrar una laptop destruida junto a una foto del padre de la familia quemada."
                            "La llave la clasificaron como 'Evidencia' y simplemente fue archivada."
                            "La Familia sigue desaparecida."
                            return
                    "Respiras hondo.":
                        jump sidestagetres
                        label sidestagetres:
                            show decImg at right
                            dec "Okey, tranquilizate, eres un gran Detective, solo piensa con calma."
                            hide decImg with dissolve
                            decP "Estás en un muy posible caso de secuestro."
                            decP "Tienes una llave con una nota."
                            decP "¡La nota!"
                            "Decides analizar cada detalle de la nota."
                            decP "Esta escrita con calma, una caligrafia elegante y con un tipo de papel similar al de un libro."
                            decP "Quien fuera que escribió esto sabia que algo pasaría."
                            decP "Okey, ya sé que ahora debo buscar una habitación que tenga lapiceros y libros."
                            "Lees la parte de atras del papel."
                            show decImg at right
                            dec "-vina Comedia."
                            dec "La Divina Comedia."
                            dec "Esto fue arrancado de un libro, una pista quizás."
                            hide decImg with dissolve
                            decP "Una habitación con librero. Perfecto, eso es fácil de buscar."
                            scene black with fade
                            "Después de buscar rápido en la casa solo queda una puerta que esta cerrada."
                            decP "¿Será que?..."
                            "Metes la llave y entra a la perfección."
                            scene despacho with fade
                            "El despacho de la casa, un lugar ordenado y con un gran librero."
                            show decImg at right
                            dec "Este es el lugar donde fue escrita la nota."
                            dec "Aquí debe de haber más pistas."
                            hide decImg with dissolve
                            "Sobre el escritorio te encuentras con una laptop desbloqueada."
                            "La laptop tiene fotografias, videos y un archivo de texto."
                            show decImg at right
                            dec "Esta persona de verdad estaba preparada para algo."
                            dec "Todo esto, es evidencia."
                            dec "A ver qué dice el archivo."
                            hide decImg with dissolve
                            show laptop at left
                            file "Espero que cuando encuentres este archivo no sea demasiado tarde."
                            file "Mi familia y yo hemos sidos secuestrados."
                            file "Desde hace años somos acosados por un exnovio de mi esposa, se ha vuelto loco."
                            file "He tratado de todo para proteger a mi familia, pero no ha sido suficiente, siempre nos encuentra."
                            file "Sospecho que hará algo esta noche."
                            file "Le dejé cartas a mi vecina para que cuando vuelva a su casa llame a la policia."
                            file "Esa persona es astuta, no sé de qué pueda ser capaz."
                            file "Por favor, encuentranos."
                            file "El nombre de esta persona es XXXX, en la laptop encontrarás fotografias de él."
                            file "Si puedes, llama la policia, procura que atrapen a este demente antes que pase algo."
                            file "Ultima Modificación: Hace 3 horas."
                            hide laptop with dissolve
                            show decImg at right
                            dec "Esto es-"
                            hide decImg
                            "Escuchas ramas rompiendose desde afuera, alguien viene hacia acá."
                            "Decides esconderte y esperar a ver quién es."
                            "Alguien entra por la ventana, no nota tu presencia, solo le interesa la laptop."
                            show stalImg at left
                            desc "Estoy seguro que ese imbécil guardó evidencia en mi contra."
                            desc "Hace de todo para separarme de {b}mi{/b} esposa."
                            hide stalImg with dissolve
                            "Reconoces a la persona, es el mismo de las fotos de la Laptop."
                            "Sacas tu arma y le apuntas."
                            show decImg at right
                            dec "No te muevas."
                            dec "Quedas bajo arresto por el secuestro de La Familia XXXX."
                            hide decImg with dissolve
                            show stalImg at left
                            desc "Oye, escuchame, escuchame, escuchame."
                            desc "Soy el {b}verdadero{/b} esposo."
                            desc "¡Estás en lo que sería {b}MI{/b} casa!"
                            desc "{b}¡Estás en mi casa!{/b}"
                            desc "yo fui quien se casó con ella."
                            desc "{b}¡YO ME CASE CON ELLA!{/b}"
                            desc "No ese imbécil."
                            hide stalImg with dissolve
                            decP "Es inestable, debo tener cuidado."
                            show decImg at right
                            dec "¡Por ultima vez!"
                            dec "¡Estas bajo arresto!"
                            hide decImg
                            "El sujeto salta por la ventana hacia el patio trasero."
                            "Vas detrás de él, si escapa podría matar a alguien."
                            scene backyard with fade
                            show decImg at left
                            dec "¡Si sigues corriendo dispararé!"
                            hide decImg
                            play sound("audio/soundS.mp3")
                            "El sujeto se detiene, sabe que hablas en serio."
                            show stalImg at right
                            desc "No lo entiendes... Ella solo me ama a mí."
                            hide stalImg with dissolve
                            show decImg at left
                            dec "No lo dudo, eres un encanto."
                            hide decImg with dissolve
                            scene black with fade
                            "Logras arrestar al acosador y llevarlo a la comisaria."
                            "Mientras lo interrogabas tu equipo logra dar con la ubicación de La Familia."
                            scene goodEnding with fade
                            "Se encontraban en un almacen a 4km del lugar de los hechos."
                            "Por las evidencias encontradas en La Laptop lográn encerrar al acosador por mucho tiempo, además de conseguirle ayuda psicológica."
                            "Todos están a salvo, gracias a ti."
                            "Felicitaciones."
                            "Gracias por Jugar."
                            return
                            