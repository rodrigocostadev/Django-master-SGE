# Define a imagem base do container (imagem é como uma iso em uma VM)
FROM python:3.12.10-slim

# Define o diretório de trabalho dentro do container.
# Cria a pasta /sge se não existir
# Todos os próximos comandos serão executados dentro dela, é como dar um cd /sge
WORKDIR /sge

# Copia todos os arquivos do seu projeto (da máquina local) para dentro do container.
COPY . .

# Impede o Python de gerar arquivos .pyc.
ENV PYTHONDONTWRITEBYTECODE 1 

# Faz o Python mostrar os logs em tempo real.
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# A LINHA A BAIXO É DESCOMENTADA QUANDO RODA O SQLITE (a migração pode rodar durante o build)
# RUN python manage.py migrate

# Informa que o container usa a porta 8000.
EXPOSE 8000

# Todos os comandos que vem antes do CMD fazem parte do build da imagem, 
# e ao rodar o comando para fazer build o CMD não é executado

# o container ainda não existe durante o build, logo não existe a rede, 
# logo se rodar o migrate não vai encontrar o banco de dados e vai quebrar a execução da aplicação

# CMD deve ser sempre o ultimo comando do dockerfile
# CMD python manage.py runserver 0.0.0.0:8000 --noreload
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000 --noreload




# Na pasta do projeto sge dar o comando: docker compose -up

# Executar o comando: docker exec -it 56a5e5001d2d /bin/bash 

# "docker exec" Esse comando permite executar comandos dentro de um container docker 
# "-it" Permite que você use o terminal como se estivesse dentro da máquina.
#  "/bin/bash" foi o comando utilizado para entrar na pasta do container

# Dar o comando: python manage.py createsuperuser             "usuario e senha é admin"  







