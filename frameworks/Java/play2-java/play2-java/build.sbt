name := "play2-java"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayMinimalJava, PlayNettyServer).disablePlugins(PlayFilters).enablePlugins(JavaAgent)

scalaVersion := "2.13.1"

libraryDependencies ++= Seq(
  guice,
  "io.kamon" %% "kamon-bundle" % "2.1.0",
  "io.kamon" %% "kamon-influxdb" % "2.1.0"
)
