from flask import Flask, render_template

app = Flask(__name__)

# Lista de cursos (você escolhe)
cursos = [
    {"nome": "Comunicação Assertiva", "descr": "Oratória, Retórica e Técnicas de Apresentação", "link": "https://www.escolavirtual.gov.br/curso/1347"},
    {"nome": "Estratégias de produtividade", "descr": "Clareza, propósito e priorização de tarefas", "link": "https://www.escolavirtual.gov.br/curso/444"},
    {"nome": "Gestão do Tempo e Produtividade", "descr": "Você sabe para onde está indo?", "link": "https://www.escolavirtual.gov.br/curso/468"},
    {"nome": "Planejamento e Organização Pessoal no Trabalho", "descr": "Ferramentas, reflexões e práticas ", "link": "https://www.escolavirtual.gov.br/curso/475"},
    {"nome": "Gestão Pessoal ", "descr": "Base da Liderança", "link": "https://www.escolavirtual.gov.br/curso/163"},
    {"nome": "Gerenciar Dados", "descr": "Aprender a gerenciar dados usando o Microsoft 365", "link": "https://www.escolavirtual.gov.br/curso/1160"},
    {"nome": "Introdução ao Excel", "descr": "Funcionalidades básicas do Excel", "link": "https://www.escolavirtual.gov.br/curso/459"},
    {"nome": "Excel Intermediário", "descr": "Funções essenciais e  vários recursos", "link": "https://www.escolavirtual.gov.br/curso/1275"},
    {"nome": "Excel Avançado", "descr": "Cálculos avançados, automação de processos com macros e programação em VBA", "link": "https://www.escolavirtual.gov.br/curso/1274"},

]

@app.route("/")
def home():
    return render_template("index.html", cursos=cursos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
