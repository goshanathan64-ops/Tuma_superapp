[app]

title = TUMA
package.name = tuma
package.domain = org.tuma
source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
version = 0.1
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 34
android.minapi = 23
android.ndk = 25b
android.arch = arm64-v8a
android.permissions = INTERNET
android.orientation = portrait