[app]
title = TUMA Super App
package.name = tuma
package.domain = com.tuma
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,ttf,db
version = 23.3
requirements = python3,kivy==2.3.0,kivymd==1.1.1,sqlite3,requests,pillow
orientation = portrait
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk_path =
android.ndk_path =
android.logcat_filters = *:S python:D
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
