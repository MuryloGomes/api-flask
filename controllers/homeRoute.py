from flask import Blueprint

homeapi = Blueprint('homeapi', __name__)

@homeapi.route('/')
def home():
    return "Bem-vindo à API de Gestão Escolar!"