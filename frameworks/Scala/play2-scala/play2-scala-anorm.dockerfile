FROM hseeberger/scala-sbt:8u242_1.3.8_2.13.1
WORKDIR /play2
COPY play2-scala-anorm .

RUN sed -i 's/.enablePlugins(PlayScala, PlayNettyServer)/.enablePlugins(PlayScala).disablePlugins(PlayNettyServer)/g' build.sbt

RUN sbt stage

ARG kamon_args=""
ENV kamon_args=$kamon_args
CMD target/universal/stage/bin/play2-scala-anorm -Dplay.server.provider=play.core.server.AkkaHttpServerProvider -J-server -J-Xms1g -J-Xmx1g -J-XX:NewSize=512m -J-XX:+UseG1GC -J-XX:MaxGCPauseMillis=30 -J-XX:-UseBiasedLocking -J-XX:+AlwaysPreTouch -Dthread_count=$(nproc) -Dphysical_cpu_count=$(grep ^cpu\\scores /proc/cpuinfo | uniq | awk '{print $4}') -Ddb_pool_size=$(( $(( $(nproc) * 2 )) + 1 )) $kamon_args
