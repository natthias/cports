pkgname = "obs-vkcapture"
pkgver = "1.5.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glslang-devel",
    "libx11-devel",
    "libxcb-devel",
    "mesa-devel",
    "obs-studio-devel",
    "simde",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
]
pkgdesc = "OBS Linux Vulkan/OpenGL game capture"
license = "GPL-2.0-only"
url = "https://github.com/nowrep/obs-vkcapture"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "02e79385f5afd6fcc0dbbcdb35adb653a111bf3a0d4d4d7edd82297222f80637"
hardening = ["!vis", "!cfi"]
# no tests
options = ["!check"]
