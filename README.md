# 🛠️ Telegram Credit Card Checker Bot

Welcome to the **Telegram Credit Card Checker Bot** project! This bot allows authorized users to upload and process credit card combos directly in Telegram. It validates cards and fetches BIN (Bank Identification Number) details using an external API, and then checks card status via a gateway.

---

## ✨ Features

- 🔒 **Restricted Access:** Only authorized users can access the bot.
- 📄 **File Upload:** Users can upload combo files for checking.
- 🌍 **BIN Information Retrieval:** Automatically fetches bank and country details.
- ✅ **Card Validation:** Verifies cards for approval or decline.
- 🛑 **Stop Processing:** Allows halting ongoing processes via inline buttons.

---

## ⚙️ Setup Instructions

Follow these steps to set up the bot:

### 1. Clone the Repository
```bash
git clone https://github.com/abirxdhackz/Mash-CC-Checker-Bot.git
cd Mash-CC-Checker-Bot
```

### 2. Install Required Libraries
Ensure you have Python 3.9+ installed. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set Up the Bot Token
Replace the placeholder `token` in `main.py` with your **Telegram Bot API Token**.

```python
token = 'your-bot-token'
```

### 4. Adjust Authorization
Add your authorized user IDs in the `subscriber` list in `main.py`:
```python
subscriber = ['user_id_1', 'user_id_2', ...]
```

### 5. Start the Bot
Run the bot using:
```bash
python main.py
```

---

## 📋 How It Works

1. **Start Command**: 
   - Users send `/start` to initialize interaction.
   - Only authorized users can proceed.

2. **Upload Combo File**:
   - Upload a `.txt` file containing card details in the format: `number|month|year|cvc`.

3. **Card Validation**:
   - Each card is validated via the gateway.
   - BIN details are fetched for additional info.

4. **Result Updates**:
   - Progress and results are displayed interactively in the chat.

5. **Stop Processing**:
   - Use the `⏹ Stop` button to halt processing at any time.

---

## ⚠️ Important Notes

- 🚨 **API Dependency**: Ensure external APIs (like BIN lookup and gateway services) are operational.
- 🔐 **Security**: Store sensitive data like tokens securely. Do not hard-code them in the script.
- ✅ **Legal Compliance**: Use this bot responsibly and in accordance with applicable laws.

---

## 💻 Example Commands

- **Start Bot**: `/start`
- **Upload File**: Drag and drop a `.txt` file into the chat.

---

## 📹 Additional Resources

- 🌐 **Bot Showcase Post**: Check out our bot post on Telegram [here](https://t.me/abir_x_official/1321).
- 📺 **YouTube Setup Tutorial**: Watch the setup tutorial on YouTube [here](https://youtu.be/34wdOSPRj74?si=UuIGqIsEcWuvF4Ye).
- 📹 **Telegram Video Tutorial**: Watch the video on Telegram [here](https://t.me/abir_x_official/1321).

---

## 🤝 Credits

- **Created By**: OGM10
- **Developed By**: [@abirxdhackz](https://t.me/abirxdhackz)

---

Feel free to customize and enhance this bot for your specific needs. 😊

Thank you for reading this repo! 🎉

