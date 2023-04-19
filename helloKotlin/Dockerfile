FROM openjdk:11
WORKDIR /app
COPY helloKotlin.kt .
RUN apt-get update && apt-get install -y curl zip && \
    curl -s https://get.sdkman.io | bash && \
    bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install kotlin && kotlinc helloKotlin.kt -include-runtime -d hello_kotlin.jar "
CMD ["java", "-jar", "hello_kotlin.jar"]