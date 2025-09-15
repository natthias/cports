pkgname = "vtsls"
pkgver = "0.3.0"
pkgrel = 0
# hostmakedepends = ["pnpm"]
hostmakedepends = ["nodejs"]
depends = ["typescript"]
pkgdesc = "LSP wrapper for the TypeScript extension from Visual Studio Code"
license = "MIT"
url = "https://github.com/yioneko/vtsls"
source = f"https://registry.npmjs.org/@vtsls/language-server/-/language-server-{pkgver}.tgz"
# source = f"{url}/archive/refs/tags/service-v0.2.8.tar.gz"
sha256 = "f065ff01476d71395caad2647fb56539bb80131f37081767b2aeee8586cbc0c9"
# sha256 = "c7acd86b2f7076f0885ec4c5ab87e0e4b9e066bc0c667bb76196e757b49495e5"


def prepare(self):
    self.do(
        "npm",
        "install",
        "--global",
        "--user",
        "root",
        "--prefix",
        "npm-out",
        self.chroot_sources_path / f"language-server-{pkgver}.tgz",
        allow_network=True,
    )
    self.rm("npm-out/lib/node_modules/root", recursive=True)


def install(self):
    self.install_files("npm-out/bin", "usr")
    self.install_files("npm-out/lib", "usr")

    self.install_license("LICENSE")


# def prepare(self):
#     self.do("pnpm", "install", allow_network=True)


# def build(self):
#     self.do("pnpm", "build")


# def install(self):
#     self.install_file("")
