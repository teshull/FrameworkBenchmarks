name := "play2-scala"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala, PlayNettyServer).disablePlugins(PlayFilters).enablePlugins(JavaAgent)

scalaVersion := "2.13.1"

libraryDependencies ++= Seq(
  guice,
  "io.kamon" %% "kamon-bundle" % "2.1.0"
)
