[app]
title = TUMA Super App
package.name = tuma
package.domain = com.tuma
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,db,json
version = 23.3
requirements = python3,kivy==3.1.0,kivymd==1.2.0,sqlite3,requests,pillow
orientation = portrait
fullscreen = 1
p4a.python_version = 3.10

# Icon and presplash (add these if you have assets)
# icon.filename = %(source_dir)s/assets/icon.png
# presplash.filename = %(source_dir)s/assets/presplash.png

# Android Configuration
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,POST_NOTIFICATIONS
android.api = 34
android.minapi = 21
android.ndk_version = 25b
android.sdk_path =
android.ndk_path =
android.logcat_filters = *:S python:D
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# Gradle dependencies for better compatibility
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1,androidx.constraintlayout:constraintlayout:2.1.4,com.google.android.material:material:1.11.0

# Release settings
android.release_artifact = apk
# android.keystore = 1
# android.keystore_path = /path/to/keystore
# android.keystore_alias = alias_name

[buildozer]
log_level = 2
warn_on_root = 1
