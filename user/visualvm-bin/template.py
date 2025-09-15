pkgname = "visualvm-bin"
pkgver = "2.2.1"
pkgrel = 0
archs = ["aarch64", "x86_64"]
depends = ["virtual:java-jre!openjdk21-jre"]
pkgdesc = "Tool for profiling and benchmarking java programs"
subdesc = "precompiled binary"
license = "GPL-2.0-only WITH Classpath-exception-2.0"
url = "https://github.com/oracle/visualvm"
source = f"https://github.com/oracle/visualvm/releases/download/{pkgver}/visualvm_{pkgver.replace('.', '')}.zip"
sha256 = "6884c908c9e10a959dea8e7b168b496515c0310d6b86a35ce96b8197231f4ef3"
options = ["!scanrundeps"]


def install(self):
    for dir in ["bin", "etc", "platform", "visualvm"]:
        self.install_files(dir, "usr/lib/visualvm")
    self.uninstall("usr/lib/visualvm/bin/visualvm.exe")

    # none of these are packaged (also compiled on foreign arch)
    self.uninstall("usr/lib/visualvm/visualvm/lib/deployed")

    # uninstall foreign objects
    match self.profile().arch:
        case "x86_64":
            self.uninstall("usr/lib/visualvm/platform/modules/lib/i386")
            self.uninstall("usr/lib/visualvm/platform/modules/lib/aarch64")
            self.uninstall("usr/lib/visualvm/platform/modules/lib/riscv64")
        case "aarch64":
            self.uninstall("usr/lib/visualvm/platform/modules/lib/i386")
            self.uninstall("usr/lib/visualvm/platform/modules/lib/riscv64")
            self.uninstall("usr/lib/visualvm/platform/modules/lib/amd64")
            self.uninstall(
                "usr/lib/visualvm/platform/modules/lib/libflatlaf-linux-x86_64.so"
            )

    self.install_dir("usr/bin")
    self.install_link(
        "usr/bin/visualvm",
        "../lib/visualvm/bin/visualvm",
    )

    self.install_file(
        self.files_path / "visualvm.png", "usr/share/icons/hicolor/96x96/apps"
    )
    self.install_file(
        self.files_path / "visualvm.desktop", "usr/share/applications"
    )

    self.install_license("LICENSE.txt")
