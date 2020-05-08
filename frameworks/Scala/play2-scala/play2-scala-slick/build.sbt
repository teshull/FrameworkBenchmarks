name := "play2-scala-slick"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala, PlayNettyServer).disablePlugins(PlayFilters).enablePlugins(JavaAgent)

scalaVersion := "2.13.1"

libraryDependencies ++= Seq(
  guice,
  "com.typesafe.play" %% "play-slick" % "5.0.0",
  "mysql" % "mysql-connector-java" % "8.0.19",
  "io.kamon" %% "kamon-bundle" % "2.1.0",
  filters
)
