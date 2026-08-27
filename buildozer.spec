[app]
title = TUMA
package.name = tuma
package.domain = org.tuma
source.dir =.
version = 23.13
requirements = python3,kivy==2.3.0,kivymd==1.2.0
orientation = portrait

[app:android]
android.api = 34
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.sdk_path = %(env.ANDROID_HOME)s