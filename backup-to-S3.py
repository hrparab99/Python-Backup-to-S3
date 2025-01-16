import datetime
import shutil
import os
import boto3

def create_backup(source_path, destination_path):
    date_name = datetime.date.today()
    backup_name = os.path.join(destination_path, f"backup1_{date_name}")
    try:
        # Create a compressed backup
        shutil.make_archive(backup_name, 'gztar', source_path)
        backup_file = f"{backup_name}.tar.gz"
        print("Backup completed:", backup_file)
        return backup_file
    except Exception as e:
        print("Backup not completed\nError:", e)
        return None

def upload_to_bucket(s3, filename, bucket_name, source_path):
    try:
        with open(source_path, 'rb') as data:
            s3.Bucket(bucket_name).put_object(Key=filename, Body=data)
        print("Backup stored to S3")
    except Exception as e:
        print("Backup not stored to S3\nError:", e)

def main():
    # Paths for local backup
    source_path = "D:/DevOps/Python-mini-projects"
    destination_path = "D:/DevOps/Python-For-Devops/Backup"

    # AWS S3 configuration
    bucket_name = "pythonfordevops"
    s3 = boto3.resource('s3')

    # Create backup
    backup_file = create_backup(source_path, destination_path)

    if backup_file:
        # Extract filename from the backup file path
        filename = os.path.basename(backup_file)
        
        # Upload backup to S3
        upload_to_bucket(s3, filename, bucket_name, backup_file)

if __name__ == "__main__":
    main()

'''
How to Use:
Replace source_path, destination_path, and bucket_name with appropriate values.
Ensure AWS credentials are configured locally (e.g., using the AWS CLI or environment variables).
Run the script to create a backup and upload it to S3.
'''