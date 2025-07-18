headers = {
   "Content-Type": "application/json"
}


user_body= {
   "firstName": "Max",
   "email": "max@example.com",
   "phone": "+11234567890",
   "comment": "Cuidado con el perro",
   "address": "8042 Lancaster Ave.Hamburg, NY"
}


# Cuerpo del kit: solo el nombre
kit_body = {
   "name": "Kit de prueba"
}

# Encabezados con token del usuario
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer '3f50bc18-24e7-4a55-8fa4-7ef3b82f229e'"
}