# Selenium Demo Exercise Solutions

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png" width="40" alt="Python Symbol">

<img src="https://selenium-python.readthedocs.io/_static/logo.png" width="40" alt="Selenium Symbol">
</p>



<div align="center">
    <img src="./automation.png" alt="Automation Image">
</div>

---
<div align="center">
<h2>Solutions of the automation exercises available at 
    <a href="https://demo.seleniumeasy.com/" target="_blank">Easy Selenium Demo</a>
</h2>
</div>



<!-- Make a table linking levels and link toward solutions-->
<div align="center">
<table>
  <thead>
    <tr>
      <th><h4>Level</h4></th>
      <th><h4>Solutions</h4></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Basic</td>
      <td><a href="./basic">Basic Challenges Solutions</a></td>
    </tr>
    <tr>
      <td>Intermediate</td>
      <td><a href="./intermediate">Intermediate Challenges Solutions</a></td>
    </tr>
  </tbody>
</table>
</div>



<!-- Make instructions on how to install and run the code-->
### Installation and Usage

1. #### Clone this GitHub repository
   
   ```bash
   git clone https://github.com/josewebdev2000/Selenium-Demo.git
   ```

2. #### (_Optional_) Create a Python virtual environment for the solutions
   
   ```bash
   python3 -m venv <your_venv_name>
   ```

3. #### Install the required dependencies from the (_requirements.txt_) file
   
   ```bash
   pip3 -r install requirements.txt
   ```

4. #### Go to the directory of interest
   
   ```bash
   cd <directory_of_interest>
   ```

   Example:
   ```bash
   cd basic
   ```

5. #### Provide required environment variables
   
   There are two environment variables that are required to run any automation script found in this project

   ```bash
   DRIVER_PATH
   ```

   This is the path to the folder that contains the web browser driver.
   Since this project uses Firefox. Then, supply the path to your <b>geckodriver</b>

   ###### Linux Command

   ```bash
   export DRIVER_PATH=<path_to_folder_of_your_geckodriver>
   ```

   ###### Windows Command

   ```bash
   set DRIVER_PATH=<path_to_folder_of_your_geckodriver>
   ```

   ```bash
   BIN_PATH
   ```

   This is the path to the executable binary of the web browser.
   Since this project uses Firefox. Then, supply the path to your <b>firefox</b> executable file.

   ###### Linux Command

   ```bash
   export BIN_PATH=<path_to_your_firefox_binary>
   ```

   ###### Windows Command

   ```bash
   set BIN_PATH=<path_to_your_firefox_binary>
   ```

   ###### Note

   If your operating system is <b>Ubuntu</b> the following values have been provided to you by default

   ```bash
   DRIVER_PATH=/usr/local/bin
   ```

   ```bash
   BIN_PATH=/usr/bin/firefox
   ```

   As a result, as long as the path to the folder to your geckodriver is <code>/usr/local/bin</code> you <b>WON'T</b> need to set up the <code>DRIVER_PATH</code> environment variable.

   Likewise, as long as the path to your firefox binary is <code>/usr/bin/firefox</code> you <b>WON'T</b> need to set up the <code>BIN_PATH</code> environment variable.

6. #### Run the challenge solution of interest
   
   ```bash
   python <solution_of_interest_file_name>.py
   ```

   Example:
   ```bash
   python simple_form_solution.py
   ```