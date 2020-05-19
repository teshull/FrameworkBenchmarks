name := "play2-java-jooq-hikaricp"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayMinimalJava, PlayNettyServer).disablePlugins(PlayFilters).enablePlugins(JavaAgent)

scalaVersion := "2.13.1"

val jOOQVersion = "3.10.3"

libraryDependencies ++= Seq(
  guice,
  javaJdbc,
  "mysql" % "mysql-connector-java" % "8.0.19",
  "org.jooq" % "jooq" % jOOQVersion,
  "io.kamon" %% "kamon-bundle" % "2.1.0",
  "io.kamon" %% "kamon-influxdb" % "2.1.0"
)
