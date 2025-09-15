pkgname = "hydroxide"
pkgver = "0.2.32"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/hydroxide"]
hostmakedepends = ["go"]
pkgdesc = "Third-party, open-source ProtonMail CardDAV, IMAP and SMTP bridge"
license = "MIT"
url = "https://github.com/emersion/hydroxide"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "14e603ff7f96e86a8f71bd5d5e7970ed9afa61d90d07472168a8e2e4e1349198"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "hydroxide.user")
