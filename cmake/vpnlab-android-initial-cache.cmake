# Temporary experiment only; do not use for production or published apps.
# Usage: cmake -C cmake/vpnlab-android-initial-cache.cmake <other platform arguments>
set(CLIENT_TARGET_NAME "VPNLab" CACHE STRING "Prototype executable")
set(CLIENT_APPLICATION_NAME "VPN Lab" CACHE STRING "Prototype display name")
set(CLIENT_SERVICE_NAME "VPNLab-service" CACHE STRING "Prototype service name")
set(CLIENT_ORGANIZATION_NAME "AcidIvZaLab" CACHE STRING "Prototype QSettings organization")
set(CLIENT_APP_INSTANCE_NAME "VPNLabInstance" CACHE STRING "Prototype singleton name")
set(CLIENT_KEYCHAIN_NAME "VPNLab-Keychain" CACHE STRING "Prototype secure storage scope")
set(CLIENT_ANDROID_PACKAGE "dev.acidivza.vpnlab" CACHE STRING "Prototype Android application ID (lookup)")
set(CLIENT_ENABLE_APP_UPDATES 0 CACHE BOOL "Disable upstream app updates in the prototype")
