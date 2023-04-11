# Discord-ChatGPT-Bot

This Python Discord bot uses the ChatGPT 3.5 Turbo API to generate text and images based on user input.

**Prerequisites** </br>
You need to have your Discord bot set up on the Discord Developer Portal with all intents and necessary permissions enabled, and your OpenAI API key ready.

You can create and configure a Discord bot at https://discord.com/developers/applications, and you can find your personal OpenAI API key at https://platform.openai.com/account/api-keys.

**Installation** </br>
1. Clone this repository: </br>
`git clone https://github.com/yourusername/your-discord-bot.git`
2. Change into the cloned directory: </br>
`cd your-discord-bot`
3. Install the required dependencies: </br>
`pip install -r requirements.txt`
4. Create a .env file with your Discord bot token and ChatGPT API key: </br>
`token={Your Discord bot token}` </br>
`api_key={Your ChatGPT API Key}` </br>
Make sure to reference the .env.example file for guidance.
5. Run the bot: </br>
`python bot.py`

**Usage** </br>
This bot's prefix for text is "!" and its prefix for images is "/". Prefix for text is unnecessary in DM channels.</br>
Use the following commands to interact with the bot:

!chat [prompt] - Generates a response to the given prompt using ChatGPT 3.5 Turbo API.</br>

/image [prompt] - Generates and sends an image based on the given prompt using ChatGPT 3.5 Turbo API.</br>

<img width="640" alt="Screenshot 2023-03-29 at 8 12 26 PM" src="https://user-images.githubusercontent.com/49298134/228702804-1f347893-3baa-4745-94e6-581c62726dc1.png">

<img width="612" alt="Screenshot 2023-03-30 at 11 26 17 AM" src="https://user-images.githubusercontent.com/49298134/228902473-62a8bc12-5ab4-484a-b468-9c96bd88e4a3.png">
