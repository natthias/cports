pkgname = "yaml-language-server"
pkgver = "1.23.0"
pkgrel = 0
hostmakedepends = ["yarn", "jq", "nodejs"]
depends = ["nodejs"]
pkgdesc = "YAML language server"
license = "MIT"
url = "https://github.com/redhat-developer/yaml-language-server"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "002e18cbf69842a1eb2b256f96a0f8acc48ae3f804e9872a096c3f0730c385e9"


def prepare(self):
    # First install dev dependencies and back them up
    self.do(
        "yarn",
        "install",
        "--frozen-lockfile",
        "--production",
        allow_network=True,
    )
    self.cp("node_modules", "node_modules_prod", recursive=True)
    # Install dev dependencies to build
    self.do(
        "yarn",
        "install",
        "--frozen-lockfile",
        allow_network=True,
    )


def build(self):
    self.do("yarn", "build")


# def check(self):
#     self.do("yarn", "test")


def install(self):
    self.install_files(
        "node_modules_prod",
        "usr/lib/mode_modules/yaml-language-server",
        name="node_modules",
    )
    self.install_files(
        "bin",
        "usr/lib/mode_modules/yaml-language-server",
    )
    self.install_files(
        "out",
        "usr/lib/mode_modules/yaml-language-server",
    )
    self.mkdir(self.destdir / "usr/bin")
    self.install_link(
        "usr/bin/yaml-language-server",
        "../lib/mode_modules/yaml-language-server/bin/yaml-language-server",
    )

    self.install_license("LICENSE")
