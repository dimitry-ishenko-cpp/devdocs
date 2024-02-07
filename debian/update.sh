#!/bin/bash
set -e

# slug -> name
to_name()
{
    echo $1 | sed -re "s/~[0-9.]+//; s/~/-/; s/gcc_cpp/g++/; s/_cpp$/-c++/; s/^gnu_//; s/_lts$//;"
}

# get items unique to $2 (ie, not in $1)
get_2_not_in_1() { echo $1 $1 $2 | tr ' ' '\n' | sort -V | uniq -u; }

dir=$(dirname $(dirname $(realpath "$0")))
cd "$dir"

cp bin/devmanage.in ./devmanage
sed -i -e "s|@DEVDOCS_INSTALL_DATADIR@|$dir|g" ./devmanage

all=$(./devmanage --all | tail -n+2 | sort -rV)
[[ -n "$all" ]] || exit 1

rem=
declare -A had
for doc in $all; do
    name=$(to_name $doc)
    [[ -n "${had[$name]}" ]] || had[$name]=1 rem+=" $doc"
done

loc=$(./devmanage --local | tail -n+2 | sed -re "s/^.*\[(.*)\]/\1/")

del=$(get_2_not_in_1 "$rem" "$loc")
if [[ -n "$del" ]]; then
    echo ABOUT TO DELETE ...
    echo $del
    sleep 3
    ./devmanage --remove $del
    echo
fi

echo UPDATE
./devmanage --update
echo

new=
for slug in $(get_2_not_in_1 "$loc" "$rem"); do
    new+=" $(to_name $slug)=$slug"
done
if [[ -n "$new" ]]; then
    echo INSTALL
    ./devmanage --install $new
    echo
fi

echo DEBIAN
cp debian/control.in debian/control
rm debian/devdocs-data-*.install 2>/dev/null || true

loc=$(./devmanage --local | tail -n+2 | cut -d' ' -f1)
for doc in $loc; do
    deb="devdocs-data-${doc//_/-}"
    cat <<EOF >> debian/control

Package: $deb
Architecture: all
Depends: \${misc:Depends},
 devdocs (= \${binary:Version})
Description: View devdocs offline in a terminal
 This package contains offline data for $doc.
EOF

    echo "usr/share/devdocs/html/$doc" > debian/$deb.install
done

rm ./devmanage
