FROM debian:jessie

# Install dependencies
RUN dpkg --add-architecture i386 && \
  	apt-get update && \
  	apt-get install -y wget bsdmainutils tmux mailutils postfix lib32gcc1 libstdc++6 libstdc++6:i386 && \
  	apt-get clean && \
  	rm -fr /var/lib/apt/lists/* && \
  	rm -fr /tmp/*

# Create user to run as
RUN groupadd -r dstserver && \
	useradd -rm -g dstserver dstserver

# Define working directory
WORKDIR /home/dstserver

USER dstserver

# Install DST Server
RUN wget http://gameservermanagers.com/dl/dstserver && \
  	chmod +x dstserver

# Expose port
# - 10999: Port to serve on
EXPOSE 10999/tcp
EXPOSE 10999/udp

# Default command
ENTRYPOINT ["./dstserver"]
