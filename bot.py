import discord
import asyncio

# Replace with your bot token
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Intents to manage bot permissions
intents = discord.Intents.default()
intents.message_content = True

# Create a bot object without using Discord commands directly
client = discord.Client(intents=intents)

# ASCII banner for the interface
banner = '''
==============================
|        Bot Interface        |
==============================
| 1] Ban a member             |
| 2] Create a webhook         |
| 3] Generate an invite link  |
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
'''

# Function to display options and wait for user input
async def show_console_menu():
    print(banner)
    while True:
        choice = input("Choose an option between 1 and 14: ")

        if choice == '1':
            await ban_member()
        elif choice == '2':
            await create_webhook()
        elif choice == '3':
            await generate_invite()
        elif choice == '4':
            await send_message()
        elif choice == '5':
            await delete_messages()
        elif choice == '6':
            await kick_member()
        elif choice == '7':
            await execute_code()
        elif choice == '8':
            await change_nickname()
        elif choice == '9':
            await show_member_info()
        elif choice == '10':
            await list_channels()
        elif choice == '11':
            await unban_member()
        elif choice == '12':
            await create_admin_role()
        elif choice == '13':
            await assign_role_to_member()
        elif choice == '14':
            await list_users()
        else:
            print("Invalid option. Try again.")

# Function to ban a member
async def ban_member():
    member_id = input("Enter the ID of the member to ban: ")
    guild = client.guilds[0]
    member = guild.get_member(int(member_id))
    if member:
        await member.ban()
        print(f"{member} has been banned.")
    else:
        print("Member not found.")

# Function to create a webhook
async def create_webhook():
    channel_id = input("Enter the channel ID to create a webhook: ")
    guild = client.guilds[0]
    channel = guild.get_channel(int(channel_id))
    if channel:
        webhook = await channel.create_webhook(name=input("Enter the webhook name: "))
        print(f"Webhook created: {webhook.url}")
    else:
        print("Channel not found.")

# Function to generate an invite link
async def generate_invite():
    channel_id = input("Enter the channel ID to generate the invite: ")
    guild = client.guilds[0]
    channel = guild.get_channel(int(channel_id))
    if channel:
        invite = await channel.create_invite(max_age=300)
        print(f"Here is an invite link: {invite.url}")
    else:
        print("Channel not found.")

# Function to list all users with their IDs
async def list_users():
    guild = client.guilds[0]
    if guild:
        print("Available users:")
        for member in guild.members:
            print(f"- {member.name} (ID: {member.id})")
    else:
        print("Guild not found.")

# Function to send a message
async def send_message():
    channel_id = input("Enter the channel ID to send the message: ")
    message = input("Enter the message to send: ")
    guild = client.guilds[0]
    channel = guild.get_channel(int(channel_id))
    if channel:
        await channel.send(message)
        print(f"Message sent to {channel.name}.")
    else:
        print("Channel not found.")

# Function to delete messages
async def delete_messages():
    channel_id = input("Enter the channel ID to delete messages from: ")
    num = int(input("How many messages to delete? (max 100): "))
    guild = client.guilds[0]
    channel = guild.get_channel(int(channel_id))
    if channel:
        await channel.purge(limit=num)
        print(f"{num} messages deleted.")
    else:
        print("Channel not found.")

# Function to kick a member
async def kick_member():
    member_id = input("Enter the ID of the member to kick: ")
    guild = client.guilds[0]
    member = guild.get_member(int(member_id))
    if member:
        await member.kick()
        print(f"{member} has been kicked.")
    else:
        print("Member not found.")

# Function to execute Python code
async def execute_code():
    code = input("Enter the Python code to execute: ")
    try:
        exec(code)
        print("Code executed.")
    except Exception as e:
        print(f"Error: {e}")

# Function to change a member's nickname
async def change_nickname():
    member_id = input("Enter the ID of the member to change nickname: ")
    new_nickname = input("Enter the new nickname: ")
    guild = client.guilds[0]
    member = guild.get_member(int(member_id))
    if member:
        await member.edit(nick=new_nickname)
        print(f"{member}'s nickname has been changed to {new_nickname}.")
    else:
        print("Member not found.")

# Function to show member info
async def show_member_info():
    member_id = input("Enter the ID of the member to show info: ")
    guild = client.guilds[0]
    member = guild.get_member(int(member_id))
    if member:
        print(f"Username: {member.name}\nID: {member.id}\nRoles: {', '.join([role.name for role in member.roles])}")
    else:
        print("Member not found.")

# Function to list all channels with their IDs
async def list_channels():
    guild = client.guilds[0]
    if guild:
        print("Available channels:")
        for channel in guild.channels:
            print(f"- {channel.name} (ID: {channel.id})")
    else:
        print("Guild not found.")

# Function to unban a member
async def unban_member():
    user_id = input("Enter the ID of the member to unban: ")
    guild = client.guilds[0]
    banned_users = await guild.bans()
    user = discord.utils.get(banned_users, user__id=int(user_id))
    if user:
        await guild.unban(user.user)
        print(f"{user.user} has been unbanned.")
    else:
        print("User not found among banned list.")

# Function to create a role with all permissions
async def create_admin_role():
    guild = client.guilds[0]
    role = await guild.create_role(name="Admin Bot", permissions=discord.Permissions.all())
    print(f"Role {role.name} created with full permissions.")

# Function to assign a role to a member
async def assign_role_to_member():
    member_id = input("Enter the ID of the member to assign role: ")
    guild = client.guilds[0]
    member = guild.get_member(int(member_id))
    if member:
        role = discord.utils.get(guild.roles, name="Admin Bot")
        if role:
            await member.add_roles(role)
            print(f"Role {role.name} assigned to {member}.")
        else:
            print("Role 'Admin Bot' does not exist.")
    else:
        print("Member not found.")

@client.event
async def on_ready():
    print(f'{client.user} is connected to Discord!')
    await show_console_menu()

client.run(TOKEN)
