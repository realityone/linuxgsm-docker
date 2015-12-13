FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies
RUN dpkg --add-architecture i386 && \
  	apt-get update && \
  	apt-get install -y wget curl bsdmainutils tmux mailutils postfix lib32gcc1 libstdc++6 libstdc++6:i386 libcurl4-gnutls-dev:i386 python && \
  	apt-get clean && \
  	rm -fr /var/lib/apt/lists/* && \
  	rm -fr /tmp/*

# Create user to run as
RUN groupadd -r dstserver && \
	useradd -rm -g dstserver dstserver

# Define working directory
WORKDIR /home/dstserver

USER dstserver

ADD ./entrypoint.py entrypoint.py

# Install DST Server
RUN wget http://gameservermanagers.com/dl/dstserver && \
  	chmod +x dstserver

# Expose port
# - 10999: Port to serve on
EXPOSE 10999/udp

# Default command
ENTRYPOINT ["python", "./entrypoint.py"]