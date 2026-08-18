[app]
title = TUMA Super App
package.name = tuma
package.domain = org.tuma
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 23.3
version.code = 1
icon = icon.png

# CRITICAL: Use kivymd from github. Don't use kivymd==2.0
requirements = python3,kivy==2.3.0,kivymd,pillow,plyer

orientation = portrait
fullscreen = 0
android.arch = arm64-v8a
android.api = 31
android.minapi = 23
android.sdk_path = 
android.ndk_path = 
android.ndk = 25b
android.enable_androidx = True

# Permissions for TUMA: Wallet, Chat, Camera, Storage
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

# This fixes 90% of build crashes
p4a.branch = master
p4a.source_dir = 

# For faster logs
log_level = 2
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
