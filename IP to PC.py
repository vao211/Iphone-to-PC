import subprocess
import os
import shutil
import tkinter as tk
from tkinter import messagebox
import sys

def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Result:")
            print(result.stdout)
        else:
            print("Error:")
            print(result.stderr)
    except Exception as e:
        print(f"Error occur: {e}")

def remove_folders_keep_files(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)
                if os.path.isfile(sub_item_path):
                    destination_path = os.path.join(directory, sub_item)


                    if os.path.exists(destination_path):
                        print(f"Tệp đã tồn tại: {destination_path}. Đang thêm số đếm vào tên tệp.")
                        base, extension = os.path.splitext(sub_item)
                        count = 1
                        while os.path.exists(destination_path):
                            destination_path = os.path.join(directory, f"{base}_{count}{extension}")
                            count += 1
                    shutil.copy2(sub_item_path, destination_path)
                    print(f"Đã sao chép tệp: {sub_item_path} vào {destination_path}")

            # Xóa folder
            shutil.rmtree(item_path)
            print(f"Đã xóa thư mục: {item_path}")

    # Xóa .AAE
    for item in os.listdir(directory):
        if item.endswith(".AAE"):
            file_path = os.path.join(directory, item)
            os.remove(file_path)
            print(f"Đã xóa tệp: {file_path}")

if __name__ == "__main__":
    print("Made by Ngài Vinh")
    #đường dẫn exe
    if getattr(sys, 'frozen', False):
        current_directory = os.path.dirname(os.path.abspath(sys.executable))
    else:
        #đường dẫn python
        current_directory = os.path.dirname(os.path.abspath(__file__))
    messagebox.showinfo("dir",current_directory)
    
    #Lỗi vì lệnh python ... 
    command = f"python \"{current_directory}\" \"This PC\Apple iPhone\Internal Storage\DCIM\" \"C:\Iphone_copy\" "
    
    dir = "C:\Iphone_copy"
    run_powershell_command(command)
    remove_folders_keep_files(dir)
    
    messagebox.showinfo("Ngài Vinh thông báo", "Ảnh và video được lưu ở thư mục Iphone_copy trong ổ C"
                        "\n\n C:\Iphone_copy "
                        "\n\n Bấm ok để mở")
    subprocess.Popen(f'explorer "{dir}"', shell=True)