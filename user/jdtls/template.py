pkgname = "jdtls"
pkgver = "1.58.0"
pkgrel = 0
hostmakedepends = [
    "git",
    "maven",
    "openjdk21",
]
depends = ["openjdk21-jre"]
pkgdesc = "Eclipse Java language server"
license = "Apache-2.0"
url = "https://github.com/eclipse-jdtls/eclipse.jdt.ls"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "213131a7e12fdad3800defafa806c3cf7dc9367fd3825f9043646e07caea44ee"


def post_prepare(self):
    # git-commit-id plugin shit
    self.do("git", "init")
    self.do(
        "git",
        "-c",
        "user.name=chimera",
        "-c",
        "user.email=chimera",
        "commit",
        "--allow-empty",
        "-m",
        "please fix your buildsystem",
    )

    self.do(
        "mvn",
        "--fail-never",
        "org.apache.maven.plugins:maven-dependency-plugin:2.8:go-offline",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )
    self.do(
        "mvn",
        "verify",
        "--fail-never",
        "-DskipTests",  # These take 20 minutes to run, no thanks
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )

    # Package once and remove built files
    # this is needed as maven cannot fetch all dependencies correctly
    self.do(
        "mvn",
        "package",
        "-DskipTests",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )
    self.rm("org.eclipse.jdt.ls.product/target", recursive=True)


def build(self):
    # cports removes .git after git patch in patch step
    # so this needs to be redone
    self.do("git", "init")
    self.do(
        "git",
        "-c",
        "user.name=chimera",
        "-c",
        "user.email=chimera",
        "commit",
        "--allow-empty",
        "-m",
        "please fix your buildsystem",
    )

    self.do(
        "mvn",
        "-o",
        "package",
        "-DskipTests",
        "-Dmaven.repo.local=/cbuild_cache/maven",
    )


def install(self):
    self.mkdir(self.destdir / "usr/share/jdtls", parents=True)
    for file in [
        "config_linux",
        "config_ss_linux",
        "plugins",
        "bin",
    ]:
        self.install_files(
            f"org.eclipse.jdt.ls.product/target/repository/{file}",
            "usr/share/jdtls",
        )

    self.mkdir(self.destdir / "usr/bin")
    self.install_link("usr/bin/jdtls", "../share/jdtls/bin/jdtls")

    self.uninstall("usr/share/jdtls/bin/jdtls.bat")
