# linux-storage-watchdog
Watchdog service to monitor the size of a directory and automatically delete objects based on FIFO

Place the .py file where you like
Edit the directoy to watch, dirToWatch and the KB limit size of directory, dirKByteLimit

Place the .service file in the /lib/systemd/system/ directory
Edit the location of the .py file in ExecStart

