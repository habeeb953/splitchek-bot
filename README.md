# SplitChek Bot 🤖

Telegram bot for the SplitChek expense-splitting application. The bot serves as the entry point for users — it responds to commands and opens the SplitChek WebApp as a Telegram Mini App.

## What it does

- Responds to `/start`, `/help`, and `/app` commands
- Opens the SplitChek WebApp via an inline button
- Runs 24/7 on Render cloud platform

## Project Structure

```
splitchek-bot/
├── bot.py           # Main bot logic
├── requirements.txt # Python dependencies
├── Procfile         # Render start command
└── README.md        # This file
```

## How to run locally

1. Clone the repository:
```bash
git clone https://github.com/habeeb953/splitchek-bot
cd splitchek-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export BOT_TOKEN=your_telegram_bot_token
export WEBAPP_URL=https://your-server-url.onrender.com/webapp
```

4. Run the bot:
```bash
python bot.py
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | Telegram bot token from @BotFather |
| `WEBAPP_URL` | URL of the SplitChek WebApp |
| `PORT` | Port for Flask server (set automatically by Render) |

## Deployment

The bot is deployed on [Render](https://render.com) as a free web service. It runs continuously without needing a local machine.

Live bot: [@splitchek_bot](https://t.me/splitchek_bot)

## Tech Stack

- **Python 3.14**
- **pyTelegramBotAPI** — Telegram bot library
- **Flask** — lightweight web server (keeps Render service alive)
- **Threading** — runs bot and Flask server simultaneously

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and open the WebApp |
| `/help` | Show list of commands |
| `/app` | Open the SplitChek WebApp |

## Related Repositories

- [SplitChek Server & WebApp](https://github.com/MeAndNoOneElse/Python_final_project) — FastAPI backend and React frontend by Андрей Ануфриев
