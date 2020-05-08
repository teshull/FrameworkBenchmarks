name := "play2-java-jpa-hikaricp"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayMinimalJava, PlayNettyServer).disablePlugins(PlayFilters).enablePlugins(JavaAgent)

scalaVersion := "2.13.1"

libraryDependencies ++= Seq(
  guice,
  javaJpa,
  "mysql" % "mysql-connector-java" % "8.0.19",
  "org.hibernate" % "hibernate-core" % "5.4.12.Final",
  "io.kamon" %% "kamon-bundle" % "2.1.0"
)

PlayKeys.externalizeResourcesExcludes += baseDirectory.value / "conf" / "META-INF" / "persistence.xml"
