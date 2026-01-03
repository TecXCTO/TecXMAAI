import subprocess
installed_list=[]
un_installed_list=[]
with open('requirements.txt', 'r') as f:
    for line in f:
        package = line.strip()
        if package and not package.startswith('#'):
            try:
                subprocess.check_call(['pip', 'install', package])
                installed_list.append(package)
                #installed_list.extend(package)
            except subprocess.CalledProcessError:
                un_installed_list.append(package)
                #un_installed_list.extend(package)
                print(f"Failed to install {package}. Skipping...")
with open('requirements_all.txt', 'r') as f:
    for line in f:
        package = line.strip()
        if package and not package.startswith('#'):
            try:
                subprocess.check_call(['pip', 'install', package])
                installed_list.append(package)
                #installed_list.extend(package)
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}. Skipping...")
                un_installed_list.append(package)
                #un_installed_list.extend(package)
with open('installed_list.txt', 'w') as f:
    #f.writelines([j + '\n' for i,j in installed_list])
    for package_list in installed_list:
        # Join characters with a delimiter (like a comma or space) for readability
        line = "".join(package_list)
        f.write(line + "\n")
    

with open('un_installed_list.txt', 'w') as f:
    #f.writelines([j + '\n' for i,j in un_installed_list])
    for package_list in un_installed_list:
        # Join characters with a delimiter (like a comma or space) for readability
        line = "".join(package_list)
        f.write(line + "\n")
print(f"Installed Python Packages List: {installed_list} \n Uninstalled Python Packages List: {un_installed_list} \n ")
