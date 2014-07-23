       
import threading
import datetime
import stddrawpygame as stddraw 
          
class ThreadClass(threading.Thread):
  def run(self):
    now = datetime.datetime.now()
    stddraw.createWindow()
    print "%s says Hello World at time: %s" % (self.getName(), now)
    
          
for i in range(2):
  t = ThreadClass()
  t.start()