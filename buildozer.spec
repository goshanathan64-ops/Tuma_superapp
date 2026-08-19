
[app]
title = TUMA Super App
package.name = tuma
package.domain = org.tuma
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 23.3
requirements = python3,kivy==2.3.0,kivymd,pillow,plyer
orientation = portrait
icon = icon.png
presplash.filename = presplash.png
presplash.color = 0,26,51,1
fullscreen = 0
android.api = 34
android.minapi = 21
android.sdk_path =
android.ndk_path =
android.arch = arm64-v8a
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA
android.logcat_filters = *:S python:D
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1