pkgname = "mangohud"
pkgver = "0.8.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dmangoapp=true",
    "-Dmangohudctl=true",
    "-Dwith_nvml=disabled",
    "-Dwith_xnvctrl=disabled",
    "-Duse_system_spdlog=enabled",
]
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
    "python-mako",
]
makedepends = [
    "dbus-devel",
    "glfw-devel",
    "glslang-devel",
    "libcxx-devel",
    "libcxxabi-devel",
    "libx11-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "spdlog-devel",
    "vulkan-headers",
    "wayland-devel",
]
depends = [
    "python-numpy",  # mangoplot
]
pkgdesc = "Vulkan and OpenGL overlay for monitoring FPS, temperatures, and more"
license = "MIT"
url = "https://github.com/flightlessmango/MangoHud"
source = (
    f"{url}/releases/download/v{pkgver}/MangoHud-v{pkgver}-Source-DFSG.tar.xz"
)
sha256 = "6198ee1545f8fe619382fbd2eb7b2ca70d09339b29e0e56a68f4986dd1920056"


def post_install(self):
    self.uninstall("usr/lib/libimgui.a")
    self.install_license("LICENSE")
