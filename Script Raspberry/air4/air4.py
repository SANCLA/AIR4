# Air4 start script
# From here, we load all the modules and start the air4 application

import sys
import subprocess
import configparser


config = configparser.ConfigParser(allow_no_value=True)
config.sections()
config.read('settings.conf')

#import settings.conf
LoadModule_Test = config['MODULES']['LoadModule_Test']
LoadModule_Update = config['MODULES']['LoadModule_Update']
LoadModule_Upload = config['MODULES']['LoadModule_Upload']
LoadModule_ReadSensors = config['MODULES']['LoadModule_ReadSensors']

if LoadModule_Test == ("yes"):
    sys.path.insert(0, './Modules')
    import air4_Test
    
    #LMUpdate = subprocess.Popen([sys.executable, "Modules\air4_Test.py"])
    #LMUpdate.communicate()

if LoadModule_Update == ("yes"):
    LMUpdate = subprocess.Popen([sys.executable, "Modules\air4_Update.py"])
    LMUpdate.communicate()

if LoadModule_Upload == ("yes"):
    LMUpload = subprocess.Popen([sys.executable, "Modules\air4_Upload.py"])
    LMUpload.communicate()

if LoadModule_ReadSensors == ("yes"):
    LMUReadSensors = subprocess.Popen([sys.executable, "Modules\air4_ReadSensors.py"])
    LMUReadSensors.communicate()
