import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Windows 7",
    'browserName': "chrome",
    'version': "50",
    'commandTimeout': 600,
    'idleTimeout': 1000,
    'prerun': {
    	'executable': "http://gist.githubusercontent.com/ndmanvar/c130ded50c20d5e7d91d5862a2edbe0a/raw/4e4049ff650458748119c0f6b3e0694301398fd8/trigger_action_vm_via_prerun.py",
    	# 'args': [ "--silent", "-a", "-q" ],
    	'background': False
    }
}
driver = webdriver.Remote(
   command_executor='http://YOUR_SAUCE_USERNAME:YOUR_SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub',
   desired_capabilities=desired_cap)


time.sleep(10)
driver.get("http://localhost:8000/somefile1")

# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
# driver.quit()