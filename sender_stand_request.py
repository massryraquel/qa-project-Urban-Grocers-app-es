import requests
import configuration
import data

#crea un nuevo usuario
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

# Función para crear el kit
def post_new_client_kit(kit_body):
   return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=data.headers)

# Ejecutar y mostrar respuesta
response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())
