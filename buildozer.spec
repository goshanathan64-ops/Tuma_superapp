[app]
title = TUMA Super App
package.name = tuma
package.domain = com.tuma
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf,db,json
version = 23.3
requirements = python3,kivy==2.3.0,kivymd==2.0.1.dev0,requests,pillow
orientation = portrait
fullscreen = 1
p4a.python_version = 3.10
p4a.arch = arm64-v8a

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/splash.jpg

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,POST_NOTIFICATIONS
android.api = 34
android.minapi = 21
android.ndk_version = 25b
android.ndk_api = 34
android.logcat_filters = *:S python:D
android.allow_backup = True
android.accept_sdk_license = True