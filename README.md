# Spotify Account Creator + Playlist Liker

**Automates Spotify account creation, likes 3 songs in a target playlist, and saves the playlist to the library.**  
Built with **Selenium + Microsoft Edge WebDriver** – **no external CAPTCHA solver**, manual solve only.

---

## Features

| Feature | Description |
|--------|-------------|
| **Random Email & Password** | Generates unique Gmail-style emails & strong passwords |
| **Full Signup Flow** | Email → Password → Name/DOB → Gender → Terms |
| **CAPTCHA Pause** | Pauses **only once** after final "Sign Up" click for manual solve |
| **Like 3 Songs** | Scrolls and clicks heart on first 3 unliked tracks |
| **Save Playlist** | Clicks "Save to Your Library" |
| **Wait 40s** | Stays on playlist page after saving |
| **Saves Credentials** | Appends `email:password` to `C:\ac\spotify_accounts.txt` |
| **Browser Stays Open** | Manual close – perfect for debugging |

---

## Requirements

| Tool | Version |
|------|--------|
| **Python** | 3.8+ |
| **Microsoft Edge** | Latest |
| **Edge WebDriver** | Matching your Edge version |
| **Python Packages** | `selenium` |

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/YOUR-USERNAME/spotify-signup-bot.git
   cd spotify-signup-bot

Install dependenciesbash

pip install selenium

Download Edge WebDriverGo to: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Download the version that matches your Edge browser
Extract and place msedgedriver.exe in:
C:\ac\msedgedriver.exe

Create folder for accountsbash

mkdir C:\ac

How to Runbash

python single.py

What Happens:Opens Spotify signup page
Fills all fields with random data
Clicks Sign Up
Pauses → You solve CAPTCHA manually
Press Enter in terminal
Goes to target playlist
Likes first 3 unliked songs
Saves playlist
Waits 40 seconds
Done – browser stays open

File Structure

spotify-signup-bot/
│
├── single.py                 Main script
├── C:\ac\                    Output folder (create manually)
│   ├── msedgedriver.exe      Edge WebDriver
│   └── spotify_accounts.txt  Created on first run
└── README.md                 This file

Target Playlisttext

https://open.spotify.com/playlist/0oVN9L5D44JyKQGQZuLyHC?si=fKuv0Mz9TeOLLxOMTydN3Q&pi=puSMc7-bQTmVY

You can change the URL in like_songs_and_save_playlist() function.
Important WarningsFor educational/testing use only
Do NOT use for spam or mass abuse
Spotify may ban accounts or IP if overused
Manual CAPTCHA solve required (no auto-bypass)
Gmail may block fake signups – use at own risk

Future Ideas (Pull Requests Welcome)Loop for 10–100 accounts
Proxy rotation
Cookie export for login reuse
Headless mode
2Captcha integration (optional)

AuthorYOUR NAME – @YOUR-USERNAMELicense

MIT License – Feel free to fork and improve.

Star the repo if it helped you!

