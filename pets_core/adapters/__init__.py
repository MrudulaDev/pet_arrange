{
    "swagger": "2.0",
    "host": "localhost:8000",
    "basePath": "/api/",
    "info": {
        "version": "1.0.0",
        "title": "Pet Arrange",
        "description": "Connects Rescued Pets in Shelters with Prospective Adopters"
    },
    "schemes": [
        "https",
        "http"
    ],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "securityDefinitions": {
        "oauth": {
            "tokenUrl": "http://auth.ibtspl.com/oauth2/",
            "flow": "password",
            "scopes": {
                "read": "read users",
                "write": "create users",
                "update": "update users",
                "delete": "delete users",
                "superuser": "super user permission"
            },
            "type": "oauth2"
        }
    },
    "definitions": {
        "CommonHttpExceptionResponse": {
            "type": "object",
            "properties": {
                "response": {
                    "type": "string"
                },
                "http_status_code": {
                    "type": "integer"
                }
            },
            "required": [
                "response",
                "http_status_code"
            ]
        }
    },
    "parameters": {
        "UpdateShelterProfile": {
            "name": "ShelterProfile",
            "in": "body",
            "description": "Update Shelter Details",
            "schema": {
                "type": "object",
                "properties": {
                    "shelter_id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "address": {
                        "type": "string"
                    },
                    "phone_number": {
                        "type": "integer"
                    },
                    "email": {
                        "type": "string"
                    }
                },
                "required": [
                    "shelter_id",
                    "name",
                    "address",
                    "phone_number",
                    "email"
                ]
            }
        },
        "CreatePet": {
            "name": "PetDetails",
            "in": "body",
            "description": "Details of the new pet",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the pet"
                    },
                    "age": {
                        "type": "integer",
                        "description": "The age of the pet"
                    },
                    "pet_category": {
                        "type": "string",
                        "description": "what animal is the pet?",
                        "enum": [
                            "Dog",
                            "Cat",
                            "Parrot",
                            "Rabbit",
                            "Others"
                        ]
                    },
                    "size": {
                        "type": "string",
                        "description": "The size of the pet (e.g., small, medium, large)",
                        "enum": [
                            "small",
                            "medium",
                            "large"
                        ]
                    },
                    "gender": {
                        "type": "string",
                        "description": "The gender of the pet"
                    }
                },
                "required": [
                    "pet_name",
                    "pet_category",
                    "size",
                    "gender"
                ]
            }
        },
        "ShelterIdInBody": {
            "name": "ShelterID",
            "in": "body",
            "description": "Id of the shelter",
            "schema": {
                "type": "object",
                "properties": {
                    "shelter_id": {
                        "type": "integer"
                    },
                    "required": [
                        "shelter_id"
                    ]
                }
            }
        },
        "PetIdPathParam": {
            "name": "pet_id",
            "in": "path",
            "required": true,
            "type": "integer"
        },
        "UpdatePetDetails": {
            "name": "PetDetails",
            "in": "body",
            "description": "Update Pet Details",
            "schema": {
                "type": "object",
                "properties": {
                    "pet_id": {
                        "type": "integer",
                        "description": "The id of the pet"
                    },
                    "name": {
                        "type": "string",
                        "description": "The name of the pet"
                    },
                    "age": {
                        "type": "integer",
                        "description": "The age of the pet"
                    },
                    "pet_category": {
                        "type": "string",
                        "description": "what animal is the pet?",
                        "enum": [
                            "Dog",
                            "Cat",
                            "Parrot",
                            "Rabbit",
                            "Others"
                        ]
                    },
                    "size": {
                        "type": "string",
                        "description": "The size of the pet (e.g., small, medium, large)",
                        "enum": [
                            "small",
                            "medium",
                            "large"
                        ]
                    },
                    "gender": {
                        "type": "string",
                        "description": "The gender of the pet"
                    }
                },
                "required": [
                    "pet_id",
                    "name",
                    "pet_category",
                    "size",
                    "gender"
                ]
            }
        },
        "filtering Params": {
            "name": "filtering Params",
            "in": "query",
            "description": "Pet Filtering Params",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the pet"
                    },
                    "age": {
                        "type": "integer",
                        "description": "The age of the pet"
                    },
                    "pet_category": {
                        "type": "string",
                        "description": "what animal is the pet?",
                        "enum": [
                            "Dog",
                            "Cat",
                            "Parrot",
                            "Rabbit",
                            "Others"
                        ]
                    },
                    "size": {
                        "type": "string",
                        "description": "The size of the pet (e.g., small, medium, large)",
                        "enum": [
                            "small",
                            "medium",
                            "large"
                        ]
                    },
                    "gender": {
                        "type": "string",
                        "description": "The gender of the pet"
                    }
                }
            }
        }
    },
    "paths": {
        "/shelter/profile/v1": {
            "put": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Update Shelter Profile",
                "operationId": "update_profile",
                "description": "Update Profile Information for a Shelter",
                "parameters": [
                    {
                        "$ref": "#/parameters/UpdateShelterProfile"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successfully Updated",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "message": {
                                    "type": "string",
                                    "description": "A success message indicating the profile update"
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Update Profile Bad Request Response",
                        "schema": {
                            "allOf": [
                                {
                                    "$ref": "#/definitions/CommonHttpExceptionResponse"
                                }
                            ],
                            "type": "object",
                            "properties": {
                                "res_status": {
                                    "type": "string",
                                    "enum": [
                                        "INVALID_SHELTER_NAME",
                                        "INVALID_ADDRESS",
                                        "INVALID_PHONE_NUMBER",
                                        "INVALID_EMAIL"
                                    ]
                                }
                            },
                            "required": [
                                "res_status"
                            ]
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "allOf": [
                                {
                                    "$ref": "#/definitions/CommonHttpExceptionResponse"
                                }
                            ],
                            "type": "object",
                            "properties": {
                                "res_status": {
                                    "type": "string",
                                    "enum": [
                                        "INVALID_SHELTER_ID"
                                    ]
                                }
                            },
                            "required": [
                                "res_status"
                            ]
                        }
                    }
                }
            }
        },
        "/pet/v1": {
            "post": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Create Pet",
                "operationId": "create_pet",
                "description": "Create a new pet for a specific shelter",
                "parameters": [
                    {
                        "$ref": "#/parameters/CreatePet"
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Successfully Created",
                        "schema": {
                            "allOf": [
                                {
                                    "$ref": "#/parameters/PetDetails"
                                }
                            ],
                            "type": "object",
                            "properties": {
                                "pet_id": {
                                    "type": "integer",
                                    "description": "The unique identifier for the created pet"
                                },
                                "message": {
                                    "type": "string",
                                    "description": "A success message indicating the pet creation"
                                }
                            },
                            "required": [
                                "pet_id",
                                "message",
                                "pet_details"
                            ]
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating unauthorized access"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating that the shelter was not found"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/shelter/pets/v1": {
            "get": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Get All Pets in a Shelter",
                "operationId": "get_all_pets",
                "description": "Retrieve a list of all pets in a particular shelter",
                "parameters": [

                ],
                "responses": {
                    "200": {
                        "description": "Success Response",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "pet_id": {
                                        "type": "integer",
                                        "description": "The unique identifier for the pet"
                                    },
                                    "pet_name": {
                                        "type": "string",
                                        "description": "The name of the pet"
                                    },
                                    "age": {
                                        "type": "integer",
                                        "description": "The age of the pet"
                                    },
                                    "breed": {
                                        "type": "string",
                                        "description": "The breed of the pet"
                                    },
                                    "size": {
                                        "type": "string",
                                        "description": "The size of the pet (e.g., small, medium, large)"
                                    },
                                    "gender": {
                                        "type": "string",
                                        "description": "The gender of the pet"
                                    }
                                },
                                "required": [
                                    "pet_id",
                                    "pet_name",
                                    "age",
                                    "breed",
                                    "size",
                                    "gender"
                                ]
                            }
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating unauthorized access"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating that the shelter was not found"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/pet/{pet_id}/v1": {
            "get": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Get Pet",
                "operationId": "get_pet",
                "description": "Retrieve details of a specific pet in a shelter",
                "parameters": [
                    {
                        "name": "pet_id",
                        "in": "path",
                        "description": "The unique identifier of the pet",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success Response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "pet_id": {
                                    "type": "integer",
                                    "description": "The unique identifier for the pet"
                                },
                                "pet_name": {
                                    "type": "string",
                                    "description": "The name of the pet"
                                },
                                "age": {
                                    "type": "integer",
                                    "description": "The age of the pet"
                                },
                                "breed": {
                                    "type": "string",
                                    "description": "The breed of the pet"
                                },
                                "size": {
                                    "type": "string",
                                    "description": "The size of the pet (e.g., small, medium, large)"
                                },
                                "gender": {
                                    "type": "string",
                                    "description": "The gender of the pet"
                                }
                            },
                            "required": [
                                "pet_id",
                                "pet_name",
                                "age",
                                "breed",
                                "size",
                                "gender"
                            ]
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating unauthorized access"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating that the pet or shelter was not found"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Update Pet",
                "operationId": "update_pet",
                "description": "Update details of a specific pet in a shelter",
                "parameters": [
                    {
                        "name": "pet_id",
                        "in": "path",
                        "description": "The unique identifier of the pet",
                        "required": true,
                        "type": "integer"
                    },
                    {
                        "name": "pet_details",
                        "in": "body",
                        "description": "Updated details of the pet",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "pet_name": {
                                    "type": "string",
                                    "description": "The name of the pet"
                                },
                                "age": {
                                    "type": "integer",
                                    "description": "The age of the pet"
                                },
                                "breed": {
                                    "type": "string",
                                    "description": "The breed of the pet"
                                },
                                "size": {
                                    "type": "string",
                                    "description": "The size of the pet (e.g., small, medium, large)"
                                },
                                "gender": {
                                    "type": "string",
                                    "description": "The gender of the pet"
                                }
                            },
                            "required": [
                                "pet_name",
                                "size",
                                "gender"
                            ]
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success Response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "pet_id": {
                                    "type": "integer",
                                    "description": "The unique identifier for the updated pet"
                                },
                                "message": {
                                    "type": "string",
                                    "description": "A success message indicating the pet update"
                                },
                                "pet_details": {
                                    "type": "object",
                                    "properties": {
                                        "pet_name": {
                                            "type": "string",
                                            "description": "The name of the pet"
                                        },
                                        "age": {
                                            "type": "integer",
                                            "description": "The age of the pet"
                                        },
                                        "breed": {
                                            "type": "string",
                                            "description": "The breed of the pet"
                                        },
                                        "size": {
                                            "type": "string",
                                            "description": "The size of the pet (e.g., small, medium, large)"
                                        },
                                        "gender": {
                                            "type": "string",
                                            "description": "The gender of the pet"
                                        }
                                    },
                                    "required": [
                                        "pet_name",
                                        "size",
                                        "gender"
                                    ]
                                }
                            },
                            "required": [
                                "pet_id",
                                "message",
                                "pet_details"
                            ]
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating unauthorized access"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating that the pet or shelter was not found"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Delete Pet",
                "operationId": "delete_pet",
                "description": "Delete a specific pet in a shelter",
                "parameters": [
                    {
                        "name": "pet_id",
                        "in": "path",
                        "description": "The unique identifier of the pet",
                        "required": true,
                        "type": "integer"
                    }
                ],
                "responses": {
                    "204": {
                        "description": "No Content",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "message": {
                                    "type": "string",
                                    "description": "A success message indicating the pet deletion"
                                }
                            },
                            "required": [
                                "message"
                            ]
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating unauthorized access"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating that the pet or shelter was not found"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/shelter/filtered_pets/v1": {
            "get": {
                "security": [
                    {
                        "oauth": [
                            "superuser"
                        ]
                    }
                ],
                "summary": "Get Filtered Pets in a Shelter",
                "operationId": "shelter_filtered_pets",
                "description": "Retrieve filtered listings of pets in a particular shelter",
                "parameters": [
                    {
                        "name": "filter_params",
                        "in": "query",
                        "description": "Filter parameters for the listings (e.g., breed, size, gender)",
                        "required": false,
                        "type": "string"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Success Response",
                        "schema": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "pet_id": {
                                        "type": "integer",
                                        "description": "The unique identifier for the pet"
                                    },
                                    "pet_name": {
                                        "type": "string",
                                        "description": "The name of the pet"
                                    },
                                    "age": {
                                        "type": "integer",
                                        "description": "The age of the pet"
                                    },
                                    "breed": {
                                        "type": "string",
                                        "description": "The breed of the pet"
                                    },
                                    "size": {
                                        "type": "string",
                                        "description": "The size of the pet (e.g., small, medium, large)"
                                    },
                                    "gender": {
                                        "type": "string",
                                        "description": "The gender of the pet"
                                    }
                                },
                                "required": [
                                    "pet_id",
                                    "pet_name",
                                    "age",
                                    "breed",
                                    "size",
                                    "gender"
                                ]
                            }
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating unauthorized access"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Not Found",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "error": {
                                    "type": "string",
                                    "description": "An error message indicating that the shelter was not found"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
