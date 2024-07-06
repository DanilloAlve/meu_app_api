# meu_app_api
Minha API
Este projeto é parte do material didático da disciplina Desenvolvimento Full Stack Básico. O objetivo é criar um MVP ao longo das aulas da disciplina, demonstrando como desenvolver uma aplicação web completa utilizando Flask e SQLAlchemy.

Como Executar
Para executar esta API, você precisará ter todas as bibliotecas Python listadas no arquivo requirements.txt instaladas. Abaixo estão os passos detalhados para configurar o ambiente e executar a API.

Passo 1: Clonar o Repositório
Primeiro, clone este repositório para o seu ambiente local:

Passo 2: Criar e Ativar um Ambiente Virtual
É altamente recomendado o uso de ambientes virtuais para isolar as dependências do projeto. Você pode utilizar o virtualenv para criar e ativar um ambiente virtual. Caso ainda não tenha o virtualenv instalado, você pode instalá-lo usando o pip:

pip install virtualenv
Agora, crie e ative o ambiente virtual:

No Windows:

virtualenv env
.\env\Scripts\activate

Passo 3: Instalar Dependências
Com o ambiente virtual ativado, instale todas as dependências necessárias listadas no requirements.txt:


pip install -r requirements.txt
Passo 4: Executar a API
Para executar a API, utilize o comando abaixo. Este comando inicia o servidor Flask na porta 5000, acessível de qualquer endereço IP local:

flask run --host 0.0.0.0 --port 5000
Modo de Desenvolvimento
Em modo de desenvolvimento, é recomendado utilizar o parâmetro --reload. Isso fará com que o servidor reinicie automaticamente sempre que houver uma mudança no código fonte:

flask run --host 0.0.0.0 --port 5000 --reload
Acessar a API
Após iniciar o servidor, abra o navegador e acesse http://localhost:5000/#/ para verificar o status da API em execução.

