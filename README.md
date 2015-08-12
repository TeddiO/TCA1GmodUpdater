# Mass TCAdmin 1 Garrysmod Updater

This was written fairly hastily as a recent SteamCMD update seems to have broken the button that allows for updating servers on a per-user basis. As a result I've thrown this together so users and hosters alike can get their servers back on if they use host a significant amount of servers (especially per user).

##Pre-requisites

This uses Python 3.4, which you can find via the Python website. As TCA1 is purely windows only (unless you decided to put yourself through the tribulations of Mono + TCA1) then that should be enough. This was tested on a Windows Server 2008 clean install and appeared to work with just the core Python package. 

##Usage

Usage is fairly simple. In the command line, just execute the following:

```
python massgmodupdater.py path/to/steamcmd path/to/users/userfiles

Example: 

python massgmodupdater.py C:/steamcmd/steamcmd.exe C:/UserFiles/USER/GameServers
```

You can reliable use it for a user that has more than one game server (eg a GMod and CSS server) as it attempts to specifically check for GMod. It will attempt to count the total amount of GMod servers and will request input from yourself before you continue. Please however make sure that **the servers you want to update are turned off first, or you may have unexpected behaviour**.

### A few inevitable questions that you'll probably end up asking -

> When updating a mass amount of servers under a user, it appears the entire thing spits out garbage or 'slurred' text!

This is expected behaviour. It's bit of a dirty script that runs numerous steamcmd windows in a single window. They won't interact with each other, but it seemed better than making a unique window pop up each time.

> How can I tell once it's finished?

Unless your servers are from ~2007 and have received 0 updates, once the output comes to a complete standstill, you should find all the servers for that user have been updated. If you hit enter and you get the typical cmd prompt, that pretty much guarantees it. 

> Is there any way to automate it across all users?

Within the confines of this script explicitly - no. You can however create another script, import this one and this will foot most of the legwork for you (albeit you may want to comment out the input check). 

##And lastly...

This script comes with no warantees / guarantees. Use at your own risk essentially. 
