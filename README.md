Inspired by [wox.plugin.putty](https://github.com/kosz78/wox.plugin.putty), this plugin let you launch [kitty](http://www.9bis.net/kitty/) sessions from Wox.

![](http://ww1.sinaimg.cn/large/5d7c1fa4jw1elz31mxr41j20m804uaa4.jpg)  

#How to use
1. Install this plugin via `wpm install kitty`
2. Edit config.json file in this plugin folder and set:
	* The the kitty folder path in your disk
	* [Optional] Change sessions_location from 'file' to 'registry'
		to search for sessions stored in the registry
3. Run the Wox command 'Restart Wox' 
4. Run the Wox command 'kitty yourSessionHere'

#Notice
* Sessions must be in a folder at the same level as kitty.exe called "Sessions" (not applicable to registry stored sessions) 
* Your executable must be named 'kitty.exe' or 'kitty_portable.exe'
