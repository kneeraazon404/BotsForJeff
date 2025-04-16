# BotsForJeff - Streamlined Bot Setup for Discord and Telegram

This document provides comprehensive instructions for setting up and running both Discord and Telegram bots.

## Prerequisites

* **Python 3.7+** installed on your system.
* **Git** installed on your system.

## Setup Instructions

### 1. Clone the Repository

First, clone the BotsForJeff repository to your local machine:

```bash
git clone [https://github.com/kneeraazon01/BotsForJeff](https://github.com/kneeraazon01/BotsForJeff)
cd BotsForJeff
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to isolate the project dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate

# Activate the virtual environment (Windows)
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all the necessary Python packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Telegram Bot Configuration

### 1. Navigate to the Telegram Bot Directory

```bash
cd telegram-dm-bot
```

### 2. Initial Configuration

Run the setup script to configure the Telegram bot. This step likely involves setting up API keys and other necessary parameters. Follow the prompts in the script.

```bash
python setup.py -c
```

### 3. User Scraping (Optional)

To scrape users for messaging, run the scraper script:

```bash
python scraper.py
```

**Note:** Ensure you understand and comply with Telegram's terms of service regarding scraping user data.

### 4. Running the SMS Bot (Direct Messaging)

To start sending direct messages via the Telegram bot, execute the following command:

```bash
python smsbot.py
```

### 5. Group Member Addition

#### a. Navigate to the Group Management Directory

```bash
cd llattes
```

#### b. Create Session (if necessary)

Run the session creator script if required for interacting with Telegram groups:

```bash
python SessionCreator.py
```

#### c. Scrape Group Members

Scrape members from a target group using the scraper script. You will likely be prompted to enter the username or invite code of the group, as demonstrated in the accompanying video.

```bash
python Scraper.py
```

#### d. Add Members to a Group

To add the scraped members (listed in `members.txt`) to your desired Telegram group, run the member adder script. You will be asked to provide the username or identifier of the destination group, as shown in the video.

```bash
python MemberAdder.py
```

## Discord Bot Configuration

### 1. Obtain Necessary Discord Credentials

Before running the Discord bot, you need to obtain the following information from your Discord application through your web browser's developer tools (inspect element), as shown in the video:

* **Server ID:** The unique identifier of your Discord server.
* **Channel ID:** The unique identifier of the specific channel you want the bot to interact with.
* **Authorization Token:** Your Discord account's authorization token. **Treat this token with extreme confidentiality as it grants full access to your account.**

### 2. Navigate to the Discord Bot Directory

```bash
cd DiscordBot
```

### 3. User Scraping (Optional)

To scrape users from the Discord server, run the scraper script:

```bash
python scraper.py
```

**Note:** Be mindful of Discord's developer terms and community guidelines regarding user scraping.

### 4. Mass Direct Messaging (Windows Only)

To send direct messages to users on Windows, execute the `discord-mass-dm.exe` file.

**Note:** This instruction specifies a `.exe` file, indicating a compiled executable likely designed for Windows. Ensure you understand the source and functionality of this executable before running it.

## Further Assistance

If you encounter any difficulties or require further clarification, please refer back to the accompanying video tutorial for a visual guide.

**Thank you!**
