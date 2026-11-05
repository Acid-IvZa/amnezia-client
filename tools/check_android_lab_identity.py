#!/usr/bin/env python3
"""Static identity checks only. This is not an APK/build/runtime/security test."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def source(relative):
    return (ROOT / relative).read_text(encoding="utf-8")

gradle = source("client/android/build.gradle.kts")
props = source("client/android/gradle.properties")
manifest = source("client/android/AndroidManifest.xml")
activity = source("client/android/src/org/amnezia/vpn/AmneziaActivity.kt")
import_activity = source("client/android/src/org/amnezia/vpn/ImportConfigActivity.kt")
qml = source("client/ui/qml/main2.qml")
cache = source("cmake/vpnlab-android-initial-cache.cmake")

required = [
    ("gradle uses configurable ID", "applicationId = clientAndroidApplicationId" in gradle),
    ("gradle prototype ID", "clientAndroidApplicationId=dev.acidivza.vpnlab" in props),
    ("manifest import action is ID-scoped", 'android:name="${applicationId}.IMPORT_CONFIG"' in manifest),
    ("manifest file provider is ID-scoped", 'android:authorities="${applicationId}.qtprovider"' in manifest),
    ("activity provider matches ID", '"${BuildConfig.APPLICATION_ID}.qtprovider"' in activity),
    ("import action matches ID", '"${BuildConfig.APPLICATION_ID}.IMPORT_CONFIG"' in import_activity),
    ("QML window title uses configured app name", "title: Qt.application.name" in qml),
    ("lab cache has prototype ID", 'set(CLIENT_ANDROID_PACKAGE "dev.acidivza.vpnlab"' in cache),
    ("upstream app updates disabled by lab cache", "set(CLIENT_ENABLE_APP_UPDATES 0 CACHE BOOL" in cache),
    ("internal JNI source package not renamed", 'namespace = "org.amnezia.vpn"' in gradle),
]
for name, ok in required:
    print(("PASS" if ok else "FAIL") + ": " + name)
if not all(ok for _, ok in required):
    raise SystemExit(1)
print("ANDROID_LAB_STATIC_IDENTITY_PASS")
