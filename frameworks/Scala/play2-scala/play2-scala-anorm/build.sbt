name := "play2-scala-anorm"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala, PlayNettyServer).disablePlugins(PlayFilters).enablePlugins(JavaAgent)

scalaVersion := "2.13.1"

libraryDependencies ++= Seq(
  guice,
  jdbc,
  "org.playframework.anorm" %% "anorm" % "2.6.5",
  "mysql" % "mysql-connector-java" % "8.0.19",
  "io.kamon" %% "kamon-bundle" % "2.1.0",
  "io.kamon" %% "kamon-influxdb" % "2.1.0"
)
