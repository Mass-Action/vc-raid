# Local Deploy


echo """

 • 𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 •

"""


rm -rf ArrayCore
git clone https://github.com/The-HellBot/ArrayCore
cd ArrayCore
virtualenv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -U -r requirements.txt
apt-get install npm -y
cp -r example.env .env
# nano .env
# python3 -m ArrayCore 
