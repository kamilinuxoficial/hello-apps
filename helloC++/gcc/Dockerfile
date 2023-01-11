FROM gcc
# Copy the current folder which contains C++ source code
COPY . /usr/src/
# Specify the working directory
WORKDIR /usr/src/
RUN g++ -o Kamilinux main.cpp
# Run the output program from the previous step
CMD ["./Kamilinux"]
