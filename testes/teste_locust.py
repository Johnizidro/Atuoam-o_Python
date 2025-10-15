from locust import HttpUser, task, between
import random

class UsuarioBase(HttpUser):
    abstract = True

    wait_time = between(1,3)

    host = "http://localhost:8000"
