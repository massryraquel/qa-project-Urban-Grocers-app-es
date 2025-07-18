import sender_stand_request
import pytest
import configuration
import data

#Para casos positivos: status 201 y coincidencia de nombres
def positive_assert(name):
    kit_body = sender_stand_request.get_kit_body(name)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

#Para casos negativos: status 400
def negative_assert(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400


# Test 1: Crear kit con nombre válido (espera 201)
def test_create_kit_with_valid_name():
    response = sender_stand_request.post_new_client_kit(data.kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == data.kit_body["name"]

# Test 2: Crear kit con nombre vacío (espera 400)
def test_create_kit_with_empty_name():
    kit = data.kit_body.copy()
    kit["name"] = ""
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 400

# Test 3: Crear kit con nombre en 1 caracter (espera 201)
def test_create_kit_with_one_character():
    kit = data.kit_body.copy()
    kit["name"] = "A"
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 201
    assert response.json()["name"] == "A"

# Test 4: Crear kit con nombre en 511 caracteres (espera 201)
def test_create_kit_with_511_characters():
    kit = data.kit_body.copy()
    kit["name"] = "A" * 511
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 201
    assert response.json()["name"] == kit["name"]

# Test 5: Crear kit con nombre en 512 caracteres (espera 400)
def test_create_kit_with_512_characters():
    kit = data.kit_body.copy()
    kit["name"] = "A" * 512
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 400

# Test 6: Crear kit con nombre con caracteres especiales (espera 201)
def test_create_kit_with_special_characters():
    kit = data.kit_body.copy()
    kit["name"] = "@#*&^%$!"
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 201
    assert response.json()["name"] == kit["name"]

# Test 7: Crear kit con nombre con espacios (espera 201)
def test_create_kit_with_spaces():
    kit = data.kit_body.copy()
    kit["name"] = "Mi kit especial"
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 201
    assert response.json()["name"] == kit["name"]

# Test 8: Crear kit sin el campo "name" (espera 400)
def test_create_kit_without_name_field():
    kit = {}
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 400

# Test 9: Crear kit con otro tipo de dato (número en lugar de string) (espera 400)
def test_create_kit_with_numeric_name():
    kit = data.kit_body.copy()
    kit["name"] = 12345
    response = sender_stand_request.post_new_client_kit(kit)
    assert response.status_code == 400
