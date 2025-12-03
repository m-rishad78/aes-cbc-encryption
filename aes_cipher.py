from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

from getpass import getpass
from os import path


class AESCipher:
    def derive_key(self, password: str, salt: bytes) -> bytes:
        return PBKDF2(password=password.encode(), salt=salt, dkLen=32, count=100000)

    def encryption(self, filename: str, password: str) -> None:
        try:
            salt: bytes = get_random_bytes(16)
            key: bytes = self.derive_key(password=password, salt=salt)

            cipher = AES.new(key=key, mode=AES.MODE_CBC)
            iv: bytes = cipher.iv

            with open(file=filename, mode="rb") as file:
                data: bytes = file.read()

            encrypted: bytes = cipher.encrypt(pad(data, AES.block_size))

            new_filename: str = f"{filename}.enc"

            with open(file=new_filename, mode="wb") as file:
                file.write(salt + iv + encrypted)

        except Exception as error:
            print(f"Error: {str(error)}")

        else:
            print("\nFile Has been Successfully Encrypted.")

    def decryption(self, filename: str, password: str) -> None:
        try:
            with open(file=filename, mode="rb") as file:
                salt: bytes = file.read(16)
                iv: bytes = file.read(16)
                data: bytes = file.read()

            key: bytes = self.derive_key(password=password, salt=salt)

            cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
            decrypted: bytes = unpad(cipher.decrypt(data), AES.block_size)

            new_filename: str = filename[:-4]

            with open(file=new_filename, mode="wb") as file:
                file.write(decrypted)

        except ValueError:
            print("\nIncorrect Password or Corrupted File.")

        except Exception as error:
            print(f"\nError: {str(error)}")

        else:
            print("\nFile Has been Successfully Decrypted.")

    def main(self) -> None:
        try:
            print("\n\t1. Encryption\n\t2. Decryption")
            option: int = int(input("\nEnter the Option: "))

            filename: str = input("Enter the Filename: ")

            if not path.exists(filename):
                print("File doesn't Exists.")
                return

            password: str = getpass("Enter the Password: ")

            match (option):
                case 1:
                    self.encryption(filename=filename, password=password)

                case 2:
                    if not filename.endswith(".enc"):
                        print("File must end with .enc")
                        return

                    self.decryption(filename=filename, password=password)

                case _:
                    print("\nInvalid option.")

        except Exception as error:
            print(f"\nError: {str(error)}")


if __name__ == "__main__":
    aes: AESCipher = AESCipher()
    aes.main()
