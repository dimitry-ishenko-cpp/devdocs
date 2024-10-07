# [devdocs](https://devdocs.io) + [fzf](https://github.com/junegunn/fzf) + [elinks](http://elinks.or.cz) = ☯

What happens when you combine _[devdocs](https://devdocs.io)_ API documentation, _[fzf](https://github.com/junegunn/fzf)_ fuzzy finder and _[elinks](http://elinks.or.cz)_ text-based browser?

![](./image/showcase.gif)

## Installation

### Binary

Debian/Ubuntu/etc:

```shell
$ sudo add-apt-repository ppa:ppa-verse/dev
$ sudo apt install devdocs
```
```shell
$ apt list devdocs-data-*
$ # find doc packages you are interested in and install them as well, eg:
$ sudo apt install devdocs-data-css devdocs-data-html
```

RaspberryPi:

```shell
$ sudo add-apt-repository -S deb https://ppa.launchpadcontent.net/ppa-verse/dev/ubuntu jammy main
$ sudo apt install devdocs
```
```shell
# install doc packages as above
```

### From source

Stable version (requires _[CMake](https://cmake.org/)_ >= 3.16, _[elinks](http://elinks.or.cz)_ >= 0.17.1, _[fzf](https://github.com/junegunn/fzf)_, _[python3](https://www.python.org/)_ with _[Pygments](https://pygments.org)_ and _[lxml](https://lxml.de)_).

```shell
$ p=devdocs v=1.0
$ wget https://github.com/dimitry-ishenko-cpp/${p}/archive/v${v}.tar.gz
$ tar xzf v${v}.tar.gz
$ mkdir ${p}-${v}/build
$ cd ${p}-${v}/build
$ cmake ..
$ make
$ make install
```

To install system-wide, change the last 3 commands above to:
```shell
$ cmake -DSYSTEM_INSTALL=ON ..
$ make
$ sudo make install
```

## Authors

* **Dimitry Ishenko** - dimitry (dot) ishenko (at) (gee) mail (dot) com

## License

This project is distributed under the GNU GPL license. See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* [devdocs](https://devdocs.io)

Share and enjoy.
