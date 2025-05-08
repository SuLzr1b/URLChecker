# URLChecker

A sharp Python tool for cybersecurity enthusiasts to check if URLs are malicious using Google Safe Browsing. URLChecker logs every scan to `log_urls.txt` and sports a hacker-style CLI with vibrant colors. No admin privileges needed—just plug in your API key and start scanning! 🛡️

## Features
- **URL Safety Check**: Verifies URLs for malicious content (e.g., phishing, malware) via Google Safe Browsing.
- **Logging**: Records all URL checks to `log_urls.txt` with status and threats.
- **Hacker CLI**: Colorful output with `colorama` and ASCII art for cyber vibes.
- **Duplicate Prevention**: Skips logging URLs already checked.
- **API Key Support**: Loads Google Safe Browsing API key securely from `.env`.

## Log Example
URLChecker saves scan results to `log_urls.txt` in the project folder. Here’s a sample:

```
https://example.com: [] = Safe
https://testsafebrowsing.appspot.com/s/phishing.html: [phishing] = Malicious
https://test.org: [] = Safe
```

Each line shows the URL, any detected threats (e.g., `[phishing]`), and the status (`Safe` or `Malicious`).

## Prerequisites
- **Google Safe Browsing API Key**:
  - Get a free API key from [Google Cloud Console](https://console.cloud.google.com/apis/library/safebrowsing.googleapis.com).
  - Create a `.env` file in the project folder with:
    ```
    SAFE_KEY=your_api_key_here
    ```

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/URLChecker.git
   cd URLChecker
   ```

2. **Install Dependencies**:
   Requires Python 3.6+. Install the libraries:
   ```bash
   pip install pysafebrowsing python-dotenv colorama
   ```

3. **Set Up the .env File**:
   - Add your Google Safe Browsing API key to `.env`:
     ```
     SAFE_KEY=your_api_key_here
     ```

4. **Run the Tool**:
   - Open a terminal (CMD, PowerShell, or any shell—no admin needed).
   - Navigate to the project folder:
     ```bash
     cd C:\Users\YourUsername\Desktop\URLChecker
     ```
   - Run:
     ```bash
     python url_checker.py
     ```

## Usage
1. **Launch the Tool**:
   - Run `python url_checker.py`.
   - You’ll see a dope ASCII banner:
     ```
      __  __       _ _      _  ___         __          ______  _     
     |  \/  |     | (_)    (_)/ _ \        \ \        / /___ \| |    
     | \  / | __ _| |_  ___ _| | | |_   _ __\ \  /\  / /  __) | |__  
     | |\/| |/ _` | | |/ __| | | | | | | / __\ \/  \/ /  |__ <| '_ \ 
     | |  | | (_| | | | (__| | |_| | |_| \__ \\  /\  /   ___) | |_) |
     |_|  |_|__,_|_|_|\___|_|\___/ \__,_|___/ \/  \/   |____/|_.__/  
     By SuLzr1b
     Malicious URL checker
     ```

2. **Check a URL**:
   - Enter a URL (e.g., `https://example.com` or `testsafebrowsing.appspot.com/s/phishing.html`).
   - The tool checks it and displays:
     - Green for safe: `The URL https://example.com looks safe!`
     - Red for malicious: `Attention! The URL https://suspicious.com can be malicious: [phishing]`
   - Results are logged to `log_urls.txt`.

3. **View Logs**:
   - Open `log_urls.txt` in the project folder to see all checked URLs, threats, and statuses.

4. **Test URLs**:
   - Use safe URLs like `https://example.com`.
   - Test malicious URLs at [https://testsafebrowsing.appspot.com/](https://testsafebrowsing.appspot.com/) (e.g., `https://testsafebrowsing.appspot.com/s/phishing.html`).

## Troubleshooting
- **"API key not found"**: Ensure `.env` exists with `SAFE_KEY=your_api_key_here`. Get a key from [Google Cloud Console](https://console.cloud.google.com).
- **"Directory not found"**: Navigate with `cd C:\Users\YourUsername\Desktop\URLChecker`. Copy the path from File Explorer.
- **"Python not found"**: Use `C:\Python39\python.exe url_checker.py` or add Python to PATH.
- **"Invalid URL"**: Include `http://` or `https://` (e.g., `https://example.com`). The tool adds `http://` if missing.
- **No logs**: Check a URL and verify `log_urls.txt` in the project folder.
- **Connection errors**: Ensure internet access and a valid API key.

## License
MIT License. See [LICENSE](LICENSE) for details.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
