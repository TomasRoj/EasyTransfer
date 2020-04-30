# EasyTransfer
Quick and easy to use command line tool.

# What it is?

This is a simple to use command line FTP tool. This can help you if you do not want to install any FTP manager because you just need to upload
few files... This works via CLI interface using Click library.

# Installation 

```shell
git clone https://github.com/TomasRoj/EasyTransfer.git
cd EasyTransfer
pip install requirements.txt
```
And you are all set!

# Basic usage

Just by passing command like this: python ftp_transfer.py --server server.name.ip --username username --password serverPass --file C:\Users\xyz\documentXYZ.xyz

```html
--server > sets server ip
--username > sets username for login
--password > sets password for login
```

You can find theese (and more in the future :D) if you type command help.
To install and run, just download the folder, locate the file on your computer and run it as usuanl with the Python 3.x.

Image 0: This is how looks the transfer after passing the command.
![Output of the command](https://github.com/TomasRoj/EasyTransfer/blob/master/image.png)

Image 1: The file transfered to your ftp server!
![Transfered file](https://github.com/TomasRoj/EasyTransfer/blob/master/imageFTP.png)

# Other info

Contributions will be very appreciated. You can do so by making an issue. Please do not make pull request if you did not make pull request 
and dont know my opinion :D.

This project was started by @TomasRoj and it is under MIT license.
