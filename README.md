# Electrolyzed Water Disinfectant Device

This is the code for the Configuration Calculation App for the [Electroylzed Water Disinfectant Device](https://www.hackster.io/350089/electrolyzed-water-disinfectant-device-27d130). The .apk file is provided, while the source code is attached in the form of the main code and design file. The Kivy library in Python 3 is required to run the source files. The app was compiled using the Buildozer utility.

# Installing the App (Android Only)
To install the app, please download the .apk file to an Android device. The app is not released on the Google Play Store, and must be installed manually.

# Running the Source Code
To run the source code, Python 3 must be installed. On Windows, the necessary Kivy packages are installed using the following: 
`pip install kivy`
`pip install kivy.deps.glew`
`pip install docutils pygments pypiwin32 kivy.deps.sdl2`

# Compiling the App (Ubuntu or OSX for Android)
[Buildozer](https://github.com/kivy/buildozer) can be used to compile all app files into a .apk file. The Buildozer specifications file is included. With all app files inside a directory, the following can be run in the directory to build the app and save the .apk file:
`buildozer android debug`
We have not built an iOS version of our app. It does not require any editing of the source code, but will require further compilation using Xcode.
