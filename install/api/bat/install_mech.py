 import subprocess

# batch_file_path = r".\install\api\bat\mech.bat"
 batch_file_path = r".\mech.bat"
arg1 = "value1"
arg2 = "value2"

try:
    subprocess.check_call([batch_file_path, arg1, arg2])
    print("Batch file executed with arguments successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
