FROM ubuntu 
# Update apps on the base image
RUN apt-get -y update && apt-get install -y

# Install the Clang compiler
RUN apt-get -y install clang

# Copy the current folder which contains C++ source code to the Docker image under /usr/src
COPY . /usr/src/

# Specify the working directory
WORKDIR /usr/src/

# Use Clang to compile the Test.cpp source file
RUN clang++ -o Kamilinux main.cpp

# Run the output program from the previous step
CMD ["./Kamilinux"]
