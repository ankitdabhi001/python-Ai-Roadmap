# 📁 ResumeBuilder AI

## 📄 Description

ResumeBuilder AI is a Python-based project that allows users to generate professional resumes in PDF format using structured user input. It demonstrates the use of Object-Oriented Programming (OOP) and the `fpdf2` library for layout and formatting.

## ✨ Features

* Collect user details: Name, Email, Phone, Skills, and Experience
* Generates clean and readable PDF resume
* Uses OOP principles via a ResumeBuilder class
* Unicode font support for emojis and symbols
* CLI-based, fully offline

## 🛠 Tech Used

* Python 3
* `fpdf2` for PDF generation
* `datetime` for timestamps
* DejaVu fonts for emoji support

---

# 📁 AI Smart Contact Book

## 📄 Description

This project is a command-line-based contact book application that uses OOP principles. Users can add, update, view, search, and delete contacts. Each contact can include multiple tags and is stored in a dynamic list.

## ✨ Features

* Add, update, delete, view, and search contacts
* Stores name, phone number, email, and tags
* CLI-based interface
* Demonstrates Python OOP and Inheritance

## 🛠 Tech Used

* Python 3
* Class-based structure with methods for each operation
* CLI/terminal interaction

---

# 📁 Offline Gmail Email Summarizer (LLM)

## 📄 Description

This offline tool connects to your Gmail inbox using IMAP, fetches the latest emails, and summarizes them using a locally hosted LLM model like DeepSeek or LLaMA via GPT4All. The model runs fully offline after download.

## ✨ Features

* Connect to Gmail using App Password
* Fetch and decode latest emails
* Extract subject, sender, and clean body content
* Summarize using local LLM (DeepSeek 7B via GPT4All)
* Save summary in terminal and optional `.txt` file
* Fully offline and secure

## 🛠 Tech Used

* Python 3
* `imaplib`, `email`, `decode_header`
* `gpt4all` Python package
* GGUF-format LLM models (DeepSeek, LLaMA)
* HuggingFace for model download
