# 🔧 Discord Bot Console Interface
# A powerful and interactive console-based Discord bot written in Python using the discord.py library. This bot allows server administrators and developers to manage servers directly from the terminal, offering a wide range of features including banning, messaging, role management, and more.

🚀 Features
This bot comes with a rich set of functionalities accessible via a numbered console menu:

Ban a member – Ban any user by entering their ID.

Create a webhook – Set up a webhook in a specified channel.

Generate an invite link – Create an invite link to any channel (valid for 5 minutes).

Send a message – Send a custom message to a specific channel.

Delete messages – Bulk delete up to 100 messages from a channel.

Kick a member – Kick a user from the server by their ID.

Execute Python code – Dynamically run Python code from the terminal.

Change nickname – Modify a user's nickname by their ID.

Show member info – Display details such as username, ID, and roles of a user.

List all channels – View all server channels with their names and IDs.

Unban a member – Revoke a ban using the user’s ID.

Create an admin role – Automatically creates a role with full admin permissions.

Assign role to member – Assign the created admin role to a user.

List all members – Display all users in the server with their IDs.

🖥️ Console Interface Preview
plaintext
Copier
Modifier
==============================

|        Bot Interface        |

==============================

| 1] Ban a member             |

| 2] Create a webhook         |

| 3] Generate an invite link |

| 4] Send a message           |

| 5] Delete messages          |

| 6] Kick a member            |

| 7] Execute code             |

| 8] Change nickname          |

| 9] Show member info         |

| 10] List all channels       |

| 11] Unban a member          |

| 12] Create admin role       |

| 13] Assign role to member   |

| 14] List all members        |

==============================

📦 Requirements

Python 3.8+

discord.py (latest version with message_content intents)

Install dependencies:

pip install -U discord.py

🔑 Setup Instructions

Create a Discord bot via the Discord Developer Portal.

Enable the necessary privileged intents:

Server Members Intent

Message Content Intent

Replace the token in the code:

TOKEN = 'YOUR_BOT_TOKEN_HERE'

Run the bot:

python bot.py

Once the bot is connected, it will display the console menu, allowing you to interact with your server.

⚠️ Security Warning

Never share your bot token publicly. It can be used to take full control of your bot. Always keep it secret and consider storing it in a .env file.

🛠️ Customization

You can expand this bot by:

Adding error handling (try/except around Discord actions)

Supporting multiple servers (instead of guilds[0])

Adding logging or a GUI

Connecting to a database for persistence
