# React Native Installation
.
## Install instructions:
Complete this tutorial:
https://medium.com/dooboolab/running-react-native-app-in-ubuntu-18-04-7d1db4ac7518

While installing Android Studio use  Classic Snap version

	--classic 
## Start Server
Navigate to project root folder & run: 

	npm start
To clear cache & run server:

>npm start -c

#### Install Dependencies:
To install all node module dependencies, run:

	npm install
	
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
	
## == Common Errors: ==
- If you face that one or more modules are missing, re-run
>npm install
- If you face something like the following when running the app on device:

![](https://i.lensdump.com/i/inCY9Z.png) 

Simply, navigate to ***root_folder/android/app/src/main/res*** and delete the ***raw*** folder and all the ***drawable-**** folders 
Then try to re-run the app again.