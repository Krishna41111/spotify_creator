
# Spotify Account Creator + Playlist Liker

**Fully automated Spotify account creation** with **random credentials**, **manual CAPTCHA solve**, **likes 3 songs**, and **saves a playlist** — all in one script.

**No external CAPTCHA solver** — **pauses only once** for you to solve it manually.

---

## Features

| Feature | Description |
|--------|-------------|
| Random Gmail-style Email | `user1234@gmail.com` |
| Strong Random Password | 12+ characters |
| Full Signup Flow | Email → Password → Name → DOB → Gender → Terms |
| **CAPTCHA Pause** | Only **after final "Sign Up"** |
| Like 3 Songs | Clicks heart on first 3 unliked tracks |
| Save Playlist | Adds playlist to "Your Library" |
| Wait 40 Seconds | Stays on playlist page |
| Save Credentials | `C:\ac\spotify_accounts.txt` |
| **Browser Stays Open** | Manual close for inspection |

---

## Requirements

- **Python 3.8+**
- **Microsoft Edge** (latest)
- **Edge WebDriver** (`msedgedriver.exe`)
- `pip install selenium`

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Krishna41111/spotify_creator.git
   cd spotify_creator

Install Seleniumbash

pip install selenium

Download Edge WebDriverVisit: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Download version matching your Edge browser
Place msedgedriver.exe in:
C:\ac\msedgedriver.exe

Create output folderbash

mkdir C:\ac

How to Runbash

python single.py

Flow:Opens Spotify signup
Fills all fields
Clicks "Sign Up"
Pauses → You solve CAPTCHA
Press Enter
Navigates to playlist
Likes 3 songs
Saves playlist
Waits 40 seconds
Done — browser stays open

Target Playlisttext

https://open.spotify.com/playlist/0oVN9L5D44JyKQGQZuLyHC?si=fKuv0Mz9TeOLLxOMTydN3Q&pi=puSMc7-bQTmVY

Change URL in like_songs_and_save_playlist() if needed.
File Output

C:\ac\
├── msedgedriver.exe
└── spotify_accounts.txt  ← email:password (one per line)

Important NotesFor educational/testing only
Do not spam — Spotify may ban accounts/IP
Manual CAPTCHA required
Gmail may block fake emails
Use residential proxies for scale (not included)

Future IdeasLoop for 50 accounts
Proxy rotation
Save cookies for login
Headless mode
2Captcha integration

AuthorKrishna41111
GitHub: [@Krishna41111
](https://github.com/Krishna (...)License

MIT License – Free to use, modify, and share.

Star this repo if it helped you!

---

### Next Steps for You

1. Go to your repo:  
   [https://github.com/Krishna41111/spotify_creator](https://github.com/Krishna41111/spotify_creator)

2. Click **"Add file" → "Create new file"**

3. Name it: `README.md`

4. Paste the entire content above

5. Commit with message: `Add README`

6. Done! Your repo now looks **professional**

---

### Optional: Add a Badge (Looks Cool)

Add this to the top of your README:

```markdown
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/selenium-4.0%2B-green)
![Status](https://img.shields.io/badge/status-working-brightgreen)

Let me know when you want:Multi-account loop version
Proxy + headless mode
Auto-login with saved cookies

Your repo is now ready to impress!
```

