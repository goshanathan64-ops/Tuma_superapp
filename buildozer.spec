[app]

title = TUMA
package.name = tuma
package.domain = org.tuma
source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 23.3
requirements = python3,kivy==2.3.0,kivymd==1.2.0
orientation = portrait
fullscreen = 0
android.arch = arm64-v8a

[buildozer]
log_level = 2

[app:android]
android.api = 34
android.minapi = 21
android.ndk = 25b
android.permissions = INTERNET
android.orientation = portrait