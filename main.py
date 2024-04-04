import openai
import config
tarea = input("cuales son tus nubes de hoy?")
openai.api_key = config.api_key
if tarea == "imagen":
  #configuracion de la API KEY

  while True:
            descripcion_foto = input("Que imagen quieres crear?")

            if descripcion_foto == "exit":
              break


            #SOLICITUD DE IMAGEN A DALL-E-3
            response = openai.images.generate(
              model="dall-e-3",
              prompt=descripcion_foto,
              size="1024x1024",
              quality="standard",
              style="natural",
              n=1,
            )

            image_url = response.data[0].url
            print(image_url)
elif tarea =="salida":
  pass


elif tarea == "texto":
  while True:
            rol = input("con quien queres hablar hoy?")

            if rol =="exit":
              break

            pregunta_usuario = input("que quieres preguntar?")
            response = openai.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[
                {
                  "role": "system",
                  "content": rol
                },
                {
                  "role": "user",
                  "content": pregunta_usuario
                }
              ],
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
            print(response.choices[0].message.content)