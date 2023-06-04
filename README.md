# Cat Detector
Motion detector with Telegram controls and notifications used to spy on my cats when I'm not at home.
## Requirements
- Webcam
- Telegram bot
- Chat ID
- Docker

### Webcam
Any webcam recognized by the computer will work.
### Telegram bot
To control and receive notifications, you will need to create a Telegram bot (using ___Botfather___ bot in Telegram for example).
### Chat ID
You don't want other people to be monitoring and viewing your cats' photos, so you'll need to create a chat on Telegram, add your bot and get the ___chat ID___ (there are many bots in Telegram that returns your ___chat ID___).
### Docker
Application is built for amd64 architecture (working in arm64 build for RPi).

Once the image is pulled, just can start it with:
~~~bash
docker run cat-detector "YOUR_BOT_TOKEN" "YOUR_CHAT_ID"
~~~

It can also be started cloning the repository, installing the dependencies (requirements.txt) and start it with:
~~~bash
python3 main.py "YOUR_BOT_TOKEN" "YOUR_CHAT_ID"
~~~