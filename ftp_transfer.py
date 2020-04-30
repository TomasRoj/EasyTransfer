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
    file_name = os.path.basename(file)
    (file_name, ext) = os.path.splitext(file_name)

    session = ftplib.FTP(server, username, password)
    print("Transfering files...")
    file = open(file,'rb')
    session.storbinary('STOR ' + str(file_name) + str(ext), file)  
    file.close()
    print(" File transferes succesfully!")
    session.quit()
    print(" Session terminated.")

transfer()
