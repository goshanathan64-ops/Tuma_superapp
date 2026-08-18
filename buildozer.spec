[app]
title = TUMA Super App
package.name = tuma
package.domain = com.tuma
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf,db,json
version = 23.3
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,pillow, cython==0.29.36
orientation = portrait
fullscreen = 1

p4a.python_version = 3.10
p4a.bootstrap = sdl2
p4a.arch = arm64-v8a

icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,POST_NOTIFICATIONS
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 34
android.logcat_filters = *:S python:D
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
