define s = Character('Silvia', color="#c8ffc8")
define y = Character('Yo', color="#c8c8ff")

image silvia sonriendo = "silvia verde sonriendo"
image silvia sorprendida = "silvia verde sorprendida"

#Variable para controlar si el jugador ha elegido videojuego o libro interactivo
default libro = False

label start:

    play music intro
        
    s "¡Hola! ¿Qué tal la clase?"

    y "Bien..."

    "No puedo admitir que no presté atención"

    y "¿Te vas a casa ya? ¿Quieres volver conmigo?"

    s "¡Claro!"    

    play music meadow fadeout 1.0 fadein 1.0

    scene bg meadow
    with fade        

    "Al poco rato, llegamos a las praderas que hay justo a las afueras del barrio donde vivimos."

    "Es un paisaje al que me he acostumbrado. El otoño es especialmente bonito aquí."

    "Cuando éramos niños, jugábamos mucho en estas praderas, así que están llenas de recuerdos."

    show silvia sonriendo at center
    with dissolve        

    play sound sonrisa

    "Se gira hacia mí y sonríe. Su mirada es tan acogedora que siento cómo se desvanecen mis nervios."

    "¡Le preguntaré...!"

    y "Mmmm... ¿Quieres...?"

    y "¿Quieres ser mi ilustradora para una novela visual?"    

    show silvia sorprendida at center
    with dissolve

    play sound sorpresa

    "Silencio."    
    
    pause 1.0

    show silvia sonriendo at center
    with dissolve

    s "¡Me pongo a ello enseguida!!!"

    s "Pero... ¿Qué es una novela visual?"

menu:

    "Es un videojuego.":
        jump videojuego

    "Es un libro interactivo.":
        jump libroInteractivo

label videojuego:

    y "Es un tipo de vieojuego que puedes jugar en ordenador o consola."    

    jump duo

label libroInteractivo:
    
    y "Es una especie de libro interactivo, que puedes leer desde el ordenador o consola."

    $ libro = True

    jump duo

label duo:

    if libro:

        "Y así, comenzamos a crear juntos nuestro primer libro interactivo."

    else:

        "Y así, comenzamos a crear juntos nuestro primer videojuego."


    "--- FIN ---"

    return

