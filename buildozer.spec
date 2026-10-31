[app] android.accept_sdk_license = True
android.skip_update = False

title = Smart GK
package.name = smartgk
package.domain = org.smartgk

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
