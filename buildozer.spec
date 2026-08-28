name: Build TUMA APK
on:
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: {java-version: '17', distribution: 'temurin'}
      - uses: actions/setup-python@v5
        with: {python-version: '3.10'}
      - run: |
          sudo apt update
          sudo apt install -y git zip unzip python3-pip ccache
      - uses: android-actions/setup-android@v3
        with: {api-level: 34, build-tools: 34.0.0, ndk-version: 25.2.9519653}
      - run: yes | sdkmanager --licenses
      - run: pip install buildozer==1.5.0 cython==0.29.33
      - run: |
          mkdir -p ~/.buildozer/android/platform
          ln -s ${ANDROID_HOME} ~/.buildozer/android/platform/android-sdk
      - run: buildozer android debug
        env: {ANDROID_SDK_ROOT: ${{ env.ANDROID_HOME }}}
      - uses: actions/upload-artifact@v4
        with: {name: TUMA-V23.22-APK, path: bin/*.apk}