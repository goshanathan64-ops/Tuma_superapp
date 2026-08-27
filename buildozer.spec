[app]

title = TUMA
package.name = tuma
package.domain = org.tuma

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,txt

version = 23.13

requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# Architecture
android.arch = arm64-v8a

# Python-for-Android
p4a.branch = master

# Permissions
# Uncomment if your app needs internet access:
# android.permissions = INTERNET