FROM teamvaders/hellbot:latest

#clonning repo 
RUN git clone https://github.com/The-HellBot/ArrayCore.gir /root/ArrayCore
#working directory 
WORKDIR /root/ArrayCore

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/ArrayCore/bin:$PATH"

CMD ["python3","-m","ArrayCore"]
