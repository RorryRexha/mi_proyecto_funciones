swagger_template = {
    "swagger": "2.0",
    "info": {
        "description": "Documentación de API101",
        "version": "1.0",
        "title": "API101"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": ["http"],
    "paths": {
        "/api/usuarios/{id}": {
            "get": {
                "summary": "Obtiene un usuario por su ID",
                "description": "Devuelve los datos de un usuario en específico mediante su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID del usuario a obtener"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Usuario encontrado",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "ID del usuario"
                                },
                                "nombre": {
                                    "type": "string",
                                    "description": "Nombre del usuario"
                                },
                                "email": {
                                    "type": "string",
                                    "description": "Correo electrónico del usuario"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Usuario no encontrado"
                    }
                }
            },
            "put": {
                "summary": "Actualiza un usuario por su ID",
                "description": "Actualiza los datos de un usuario específico mediante su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID del usuario a actualizar"
                    },
                    {
                        "name": "usuario",
                        "in": "body",
                        "required": True,
                        "description": "Objeto JSON con los datos del usuario a actualizar",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "nombre": { "type": "string" },
                                "email": { "type": "string" }
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Usuario actualizado"
                    },
                    "404": {
                        "description": "Usuario no encontrado"
                    }
                }
            },
            "delete": {
                "summary": "Elimina un usuario por su ID",
                "description": "Elimina un usuario específico mediante su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID del usuario a eliminar"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Usuario eliminado"
                    },
                    "404": {
                        "description": "Usuario no encontrado"
                    }
                }
            }
        },
        "/api/usuarios": {
            "post": {
                "summary": "Crea un nuevo usuario",
                "description": "Crea un nuevo usuario con los datos proporcionados",
                "parameters": [
                    {
                        "name": "usuario",
                        "in": "body",
                        "required": True,
                        "description": "Datos del usuario a crear",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "nombre": { "type": "string" },
                                "email": { "type": "string" }
                            }
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Usuario creado exitosamente"
                    }
                }
            }
        }
    }
}