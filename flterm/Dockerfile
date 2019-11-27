FROM ubuntu
RUN apt update && apt install wget build-essential unzip --assume-yes; \
    cd /root && wget https://codeload.github.com/timvideos/flterm/zip/master && unzip master; \
    cd flterm-master && make; \
    mv flterm /bin/; \
    apt remove wget build-essential unzip --assume-yes; \
    apt autoremove --assume-yes
ENTRYPOINT ["flterm"]
CMD ["--help"]
