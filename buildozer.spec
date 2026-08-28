[app]
title = TUMA
package.name = tuma
package.domain = org.tuma
source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,json,txt
version = 1.0.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

[app:android]
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True