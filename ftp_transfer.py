import ftplib
from ftplib import FTP
from pyfiglet import figlet_format
import click
import os

print(figlet_format("EasyTransfer"))
print("\n An easy way to tranfer all your files into remote FTP server. \n Quick settings, quick the transfer itself. \n")
#domain name or server ip:

@click.command()
@click.option("--server", help="Specifies the server IP adress.")
@click.option("--username", help="Sets the user name for login to server.")
@click.option("--password", help="Sets the password for login to the server.")
@click.option("--file", help="Set path to file you want to transfer")

def transfer(server, username, password, file):
    file_extension = os.path.splitext(file)[1]

    session = ftplib.FTP(server, username, password)
    file = open(file,'rb')
    session.storbinary('STOR transferedFile' + str(file_extension), file)  
    file.close()
    print(" File transferes succesfully! Quiting session...")
    session.quit()
    print(" Session terminated.")

transfer()
