# Python-Backup-to-S3 🚀

A Python script that automates the creation of compressed backups of a specified directory and uploads them to an AWS S3 bucket. 🌐☁️

## Features ✨
- **Backup Creation**: Compresses a specified directory into a `.tar.gz` archive. 📦
- **Upload to S3**: Uploads the backup to an AWS S3 bucket for safe storage. ☁️
- **Error Handling**: Gracefully handles errors with informative messages. ⚠️

## Requirements 📋
- Python 3.x 🐍
- `boto3` library (Install via `pip install boto3`) 🔧
- AWS credentials configured locally (via AWS CLI or environment variables) 🌟

## Setup 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Python-Backup-to-S3.git
