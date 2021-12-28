# os_scanner
Simple scanner that's collects some information about current operating system.
All results are displayed on screen and also writes to file "results.txt". If file "results.txt" not exists it will be created. If file already exists it will be overwritten.
Also the script take screenshot (may be useful if system running with graphical interface).

1. Clone the repository with command:
   ```shell
   git clone https://github.com/AlexFromMoscow6/os_scanner.git
   ```
2. Go to directory:
   ```shell
   cd os_scanner/
   ```
3. To run scanner script you need to install scrot - a package which is used to take screenshots from the command line on Linux. Also needed python3-tk and python3-dev packages. Run additional_packages.sh script to install these packages on your system:
   ```shell
   ./additional_packages.sh
   ```
4. After that install Python dependencies:
   ```shell
   pip3 install -r requirements.txt
   ```
5. And run the script:
   ```shell
   python3 os_scanner.py
   ```
