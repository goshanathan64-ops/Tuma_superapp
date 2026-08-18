[app]
title = TUMA Super App
package.name = tuma
package.domain = org.tuma
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 23.3
requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/master.zip,pillow,plyer
orientation = portrait
fullscreen = 0
android.arch = arm64-v8a
android.api = 31
android.minapi = 23
android.ndk = 25
android.sdk_path = /home/runner/buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/buildozer/android/platform/android-ndk-r25b
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE
android.enable_androidx = True
android.logcat_filters = *:S python:D
p4a.branch = master
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
