# linux-storage-watchdog
Watchdog service to monitor the size of a directory and automatically delete objects based on FIFO

<br/>Place the .py file where you like<br/>
Edit the directory to watch, *dirToWatch* and the KB limit size of directory, *dirKByteLimit*<br/><br/>

Place the .service file in the */lib/systemd/system/* directory<br/>
Edit the location of the .py file in *ExecStart*<br/><br/>

```sudo systemctl daemon-reload  
sudo systemctl enable storageWatchdog.service  
sudo systemctl start storageWatchdog.service```
