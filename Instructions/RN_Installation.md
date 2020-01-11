# React Native Installation
This guide is supposed to demonstrate how to install & setup React Native in Ubuntu 18.04.
## Install instructions:
Complete this tutorial:
https://medium.com/dooboolab/running-react-native-app-in-ubuntu-18-04-7d1db4ac7518

Install Node.js:

	sudo apt-get install nodejs

#### Install **nvm**
	
	sudo apt-get update

Install** c++ compiler**.* It may already exists, but just in case.*
	
	apt-get install build-essential libssl-dev

Install nvm
	
	curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

Reload bash
	
	source ~/.bashrc

After installation close and reopen terminal and check nvm version
>	nvm --version

#### Install **node**

Install latest node

	nvm install node

Set default node version for nvm

	nvm alias default node

Check version of node and npm
	
	node -v
	npm -v
	
### Install Android Studio

#### Install Java

	sudo apt install openjdk-8-jre openjdk-8-jdk

#### Install android studio
In ubuntu 18.04, snap command is provided which is 
containerised software packages that are simple to create and 
install on all linux distributions.
https://snapcraft.io/

	sudo snap install android-studio --classic 

While installing Android Studio use  Classic Snap version

	--classic 
	
Configure build path in your *.bash_profile* or *.zshrc*

	export ANDROID_HOME=$HOME/Android/Sdk
	export PATH=$PATH:$ANDROID_HOME/tools
	export PATH=$PATH:$ANDROID_HOME/tools/bin
	export PATH=$PATH:$ANDROID_HOME/platform-tools
	export PATH=$PATH:$ANDROID_HOME/emulator
	
Now check whether the paths were exported using: 

>	echo $PATH

Set alias to shorten command to run emulator
	
>	alias run-emu="$ANDROID_HOME/tools/emulator @pixel2"

Reload *bash_profile* or *.zshrc*

`source ~/.bash_profile` or `source ~/.zshrc`
	
#### Generate emulator & run emulator
Note:
  - In order to make `avdmanager` command to work, you should
    start android-studio and complete installation first.
  - Also system-images should be installed Type below command to 
    install the system image.
>	sdkmanager --install "system-images;android-27;google_apis;x86"

Create `avd` device
	
	avdmanager create avd -n device1 -k "system-images;android-27;google_apis_playstore;x86" --device 'Nexus 5X
	
List emulators. You will see device1 as a result.

	emu -avd -list-avds
	
Run emulator
	
	emu -avd device1
	
## Install react-native

Install `react-native-cli` using npm.

	npm install -g react-native-cli

Create `react-native` project via `react-native-cli`.

	react-native init NewProject
	cd NewProject

#### Install Dependencies:
To install all node module dependencies, run:

	npm install
	
### Start Server
Navigate to project root folder & run: 

	npm start
To clear cache & run server:

>npm start -c

## Run React Native app on emulator/local device:
According to [official documentation](https://facebook.github.io/react-native/docs/running-on-device) , after starting the local server, run:

	react-native run-android

**To run the app on a specific device:**
Firstly, Find the device or emulator connected to PC

	adb devices
	
	List of devices attached
	$device_name    device

Then, run the app specifically to that device

	react-native run-android --deviceId=$device_name

## ==  Common Errors:  ==
- Trouble shooting with permission (Mostly seen on Android Studio):	

		sudo apt install qemu-kvm
		sudo adduser <your_username> kvm
		sudo chown <your_username> /dev/kvm
	
- If we face the following error:
![](https://i.lensdump.com/i/iUIHqx.png) 

>	Sunday, 05. January 2020 12:26pm 
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p

- If you face that one or more modules are missing, re-run
>npm install
- If you face something like the following when running the app on device:

![](https://i.lensdump.com/i/inCY9Z.png) 

Simply, navigate to ***root_folder/android/app/src/main/res*** and delete the ***raw*** folder and all the ***drawable-**** folders 
Then try to re-run the app again.

- If you face static image files missing in your bundled application, simply run this command:

> react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/

Then run the following command to compile your app to APK file.

> cd android && ./gradlew clean assembleDebug