# Android VPN Lab — isolated prototype preparation, 2026-11-05

**Status: PREPARED / static checks only. Not built, not installed, no VPN connectivity tests.**
**Branch:** `experiment/android-vpnlab-20261105`, fork `Acid-IvZa/amnezia-client`; upstream/dev `ac175c8a8147cfe56f98c8372ec17ea2ba00bb02` remains unmodified.
**Scope:** Only code in this experimental Git branch. No VPS4/VPS3, MagicBook installations, client VPN profiles or secrets changed.

## Why and what is changed

The normal AmneziaVPN client uses the Android install identity `org.amnezia.vpn`. A prototype using that same identity could conflict with the installed official client. **Temporary identifier:** `dev.acidivza.vpnlab`; this is not the future commercial name.
- `client/android/gradle.properties`: prototype-only `clientAndroidApplicationId=dev.acidivza.vpnlab`.
- `client/android/build.gradle.kts`: Gradle's `applicationId` reads `clientAndroidApplicationId`, defaulting to the original value if not supplied. Do **not** change `namespace=org.amnezia.vpn` (Kotlin packages and native JNI depend on it).
- `client/android/AndroidManifest.xml`: the import action and FileProvider authority use `${applicationId}` placeholders, avoiding cross-application collisions.
- `client/android/src/org/amnezia/vpn/AmneziaActivity.kt` and `ImportConfigActivity.kt`: corresponding runtime values use `BuildConfig.APPLICATION_ID`; Kotlin's internal package stays original.
- `client/ui/qml/main2.qml`: window title comes from `Qt.application.name` rather than a hardcoded product title.
- `cmake/vpnlab-android-initial-cache.cmake`: experimental `VPN Lab` app identity, separate settings/keychain, and `CLIENT_ENABLE_APP_UPDATES=0` to avoid the original Amnezia update channel in a lab build.

No VPN protocol, crypto code, UFW, keys or server API was modified. Existing Amnezia visual assets and certain external API links remain: **this is not a completed brand or independently safe distributable app**.

## Read-only static validation

From the repo root: `python tools/check_android_lab_identity.py`.
It checks identity wiring only. It does **not** prove Gradle or Qt builds, manifest merger correctness, absence of remote API calls or VPN runtime safety.

## Later isolated build, NOT performed or authorized here

1. Confirm disk/memory/toolchain, obtain permission before installing Qt 6.10+, CMake, Conan, platform SDK/NDK, fetching large dependencies or starting CI with costs.
2. Use an isolated workspace cloned from this exact feature branch with Git submodules. For Qt Android configure use the prototype cache `-C cmake/vpnlab-android-initial-cache.cmake` and check Android generated Gradle project actually carries `clientAndroidApplicationId=dev.acidivza.vpnlab`. If not, set it explicitly with Gradle `-PclientAndroidApplicationId=dev.acidivza.vpnlab`.
3. Build an **OSS Debug** APK, not the Play/Billing variant; do not sign/publish a release.
4. BEFORE installation, inspect the generated APK via `aapt`/apkanalyzer to confirm package ID, manifest import action, file provider authority, label, service components, app icon and permissions. Confirm all are isolated and no original service or existing app data will be overwritten.
5. BEFORE network use, disable/isolate Amnezia Gateway subscription/news/analytics, update URLs and any unintended external endpoints; review logs, TLS and permissions. Disabling app update checks alone does **not** isolate the other Amnezia API calls.
6. Run the app only on a separate test Android device/emulator with no production VPN profile; create a dedicated testing peer on a separate test VPS in a separately approved phase; verify AWG 3.1 handshakes, DNS/IP/IPv6, MTU, reconnect and kill switch without exposing real secrets in GitHub or logs.
7. Verify license/SBOM and app-store policy before external distribution. All branding is temporary; independent logos, icons and names are later work.

## Baseline MagicBook check

Read-only check 2026-11-05: MagicBook has Android Studio directory and Android SDK directory. No `cmake`, `ninja`, `conan`, `java`, `adb`, `sdkmanager`, `qmake` or `qtpaths` command was found **on PATH**; `python` and `git` were found. Android Studio may bundle some tools; no installation or download was initiated. Free C drive ~47.98 GB at check time.

## Rollback / restrictions

Feature branch is isolated from `dev`, which remains on the upstream commit. Discard the experimental branch to revert code changes. Never merge this prototype branch into the main branch before build/test/review gates. Never operate VPS4/VPS3 or use production VPN profiles during this phase.
