[app]
title = TUMA
package.name = tuma
package.domain = org.tuma
source.dir =.
version = 1.0.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0
orientation = portrait

[app:android]
android.api = 34
android.minapi = 21
android.sdk_path = %(env.ANDROID_SDK_ROOT)s
android.ndk_path = %(env.ANDROID_HOME)s/ndk/25.2.9519653
android.build_tools_version = 34.0.0
android.p4a_dir = 
android.accept_sdk_license = True
android.use_setup_android = True