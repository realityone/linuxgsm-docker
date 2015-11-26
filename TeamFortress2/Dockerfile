FROM debian:jessie

# Install dependencies
RUN dpkg --add-architecture i386 && \
  	apt-get update && \
  	apt-get install -y wget bsdmainutils tmux mailutils postfix lib32gcc1 libstdc++6 libstdc++6:i386 && \
  	apt-get clean && \
  	rm -fr /var/lib/apt/lists/* && \
  	rm -fr /tmp/*

# Create user to run as
RUN groupadd -r tf2server && \
	useradd -rm -g tf2server tf2server

# Define working directory
WORKDIR /home/tf2server

USER tf2server

# Install TF2 Server
RUN wget http://gameservermanagers.com/dl/tf2server && \
  	chmod +x tf2server

RUN ./tf2server auto-install

# Expose port
# - 27015: Port to serve on
EXPOSE 27015/tcp
EXPOSE 27015/udp

# Default command
ENTRYPOINT ["./tf2server"]
CMD ["start"]
