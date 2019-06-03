#Here is the answer
## Preparetion
1. Install python (3.6.5 not 3.7 version!!!) and add python path to your laptop environment path. 
   You can test it when you use cmd and type python-v in your Windows Command Prompt. 
   It should show your python version, otherwise you didn't add the path in your enviroment path correctly.
2. pip install virtualenv
3. cd your desktop and type: virtualenv virtual_workspace 
   (There is gonna be a file name which name is virtual_workspace shown on your desktop).
4. activate your vitrual enviroment by typing: cd virtual_workspace and then cd Scripts and then type activate. 
   (You gonna see <virtual_workspace>shows at the beginning of the command line, otherwise you didn't activate it properly).
5. install the scrapy in your virtual environment: 
   cd ..(back to the virtual_workspace path) and then typing: pip install scrapy.
6. download the Visual Studio Code. And then add python, excel viewer and json viewer extensions in your VS.
7. control+shift+p: open the workspace settings. 
   add the python vitual_workspace path by typing: 
   {
    "python.pythonPath": "C:\\Users\\Administrator\\Desktop\\virtual_workspace\\Scripts\\python.exe"
	}
   (It gonna show at the right bottom "virtual_workspace: virtualenv" otherwise you didn't set the python path correctly.)
 8. create your project file by typing:
 	scrapy startproject third_assignment(in the vitrual environment and it gonna appear in your virtual_workspace folder).
 9. create your spider quotes.py inside the spiders folder which is inside third_assignment.
 10. finally cd spiders and then pip install pylint.

Part 1 & 2: 
## Change the setting.py
   add FEED_EXPORT_ENCODING = "UTF-8" in the settings.py file (change the encoding to UTF-8).
## Change the item.py
   see it in the item.py file
## Add your quotes.py
   see it in the quotes.py file
## Run your spider:
   control+shift+p: create terminal
   type inside the terminal: scrapy crawl quotes -o data.json
   
Part 3:
## Download, install and setup MongoDB
1. The link is here: https://www.mongodb.com/download-center/community. Choose the community server's version and OS which is suit you.
2. add mongodb path to your system environment path (sep).
3. cmd type 'mongod' (tset if you add it to your sep).
4. type md "\data\db" "\data\log" (create two folders in your C drive and store your extracted data there).
5. type mongod --dbpath="C:"\data\db" (let mongodb knows that you want to store your data there).	
   If everything you setup correctly, you will be able to see 'waiting for connection on port 27017'.
 
THE MONGODB SERVER NEEDS TO RUN IN THE BACK!!! DO NOT CLOSE IT!!!

6. In Visuo Studio Code, under the virtual environment: pip install pymongo.
7. Install extension: Azure Cosmos DB (Microsoft).

   



