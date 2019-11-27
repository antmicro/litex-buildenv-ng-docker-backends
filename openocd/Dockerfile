FROM ubuntu
RUN apt update && apt install git autoconf automake pkg-config texinfo libusb-1.0.0-dev libtool build-essential --assume-yes; \
    git clone git://repo.or.cz/openocd.git; \
    cd openocd; \
    mv tcl/target/1986ве1т.cfg tcl/target/1986be1t.cfg; \
    mv tcl/target/к1879xб1я.cfg tcl/target/k1879x61r.cfg; \
    ./bootstrap; \
    mkdir build && cd build; \
    ../configure \
  --prefix=$PREFIX \
  --enable-static \
  --disable-shared \
  --enable-usb-blaster-2 \
  --enable-usb_blaster_libftdi \
  --enable-jtag_vpi \
  --enable-remote-bitbang;\
  make && make install
ENTRYPOINT ["openocd"]
CMD ["--help"]
