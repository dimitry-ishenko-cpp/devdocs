# devdocs – offline DevDocs in your terminal ⚡️

Combine [**DevDocs API documentation**](https://devdocs.io), the [**fzf fuzzy
finder**](https://github.com/junegunn/fzf), and the [**elinks text-based
browser**](http://elinks.or.cz)—all within your terminal. ☯

![LOADING...](./image/showcase.gif)

## 🚀 Why Use It?

* 🔎 **Lightning-fast search:** Use _fzf_ to filter docs instantly.
* 🛠 **Offline-friendly:** Access 100+ documentation sets including HTML, CSS,
  JS, Python, C++, and more.
* 🖥 **Terminal-native:** Works without a GUI using _elinks_.

## ⚙️ Usage

**devdocs** consists of three command-line tools:

* 🔭 **devopen** — Open a documentation entry or topic index.

<pre><code>Usage: <em>devopen</em> [-p|--preview] [<em>topic</em>] [<em>entry</em>]
   or: <em>devopen</em>  -h|--help
   or: <em>devopen</em>  -v|--version

If <em>topic</em> is omitted or set to ?, the entry will be searched
in all available topics.

If <em>entry</em> is omitted, index page for the given topic will be shown.
</code></pre>

* 🔍 **devgrep** — Fuzzy search for entries across one or all documentation topics.

<pre><code>Usage: <em>devgrep</em> [-p|--preview] [<em>topic</em>] [<em>pattern</em>]
   or: <em>devgrep</em>  -h|--help
   or: <em>devgrep</em>  -v|--version

If <em>topic</em> is omitted or set to ?, the pattern will be searched in
all available topics.

If <em>pattern</em> is omitted, all entries for the given topic will be searched.
</code></pre>

* 🧰 **devmanage** — Install, remove, and update documentation topics.

<pre><code>Usage: devmanage -a|--all
   or: <em>devmanage</em> -l|--local
   or: <em>devmanage</em> -u|--update
   or: <em>devmanage</em> -i|--install <em>topic</em> [<em>topic</em>] ...
   or: <em>devmanage</em> -r|--remove  <em>topic</em> [<em>topic</em>] ...
   or: <em>devmanage</em> -h|--help
   or: <em>devmanage</em> -v|--version

Where:
    -a|--all        Show all topics available online.
    -l|--local      Show locally cached topics.
    -u|--update     Update all local topics.

    -i|--install    Cache one or more topics locally.
    -r|--remove     Remove local topic(s).
</code></pre>

You can use the _--preview_ option with both **devgrep** and **devopen**:

![LOADING...](./image/preview.gif)

## 📦 Installation

### Binary

Debian/Ubuntu/etc:

```shell
sudo add-apt-repository ppa:ppa-verse/devdocs
sudo apt install devdocs
```

```shell
# find doc packages you are interested in and install them as well, eg:
apt list devdocs-data-*
sudo apt install devdocs-data-css devdocs-data-html
```

RaspberryPi:

```shell
$ sudo add-apt-repository -S deb https://ppa.launchpadcontent.net/ppa-verse/devdocs/ubuntu jammy main
$ sudo apt install devdocs
```

```shell
# install doc packages as above
```

### From source

Stable version (requires _[CMake](https://cmake.org/)_ >= 3.16, _[elinks](http://elinks.or.cz)_ >= 0.17.1, _[fzf](https://github.com/junegunn/fzf)_, _[python3](https://www.python.org/)_ with _[Pygments](https://pygments.org)_ and _[lxml](https://lxml.de)_).

```shell
$ p=devdocs v=1.1.4
$ wget https://github.com/dimitry-ishenko-cpp/${p}/archive/v${v}.tar.gz
$ tar xzf v${v}.tar.gz
$ mkdir ${p}-${v}/build
$ cd ${p}-${v}/build
$ cmake ..
$ make
$ make install
```

To install system-wide, change the last 3 commands above to:
```bash
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
