#!/usr/bin/python3

import sys
import os


frameworks = [
    "play2-java",
    "play2-java-ebean-hikaricp",
    "play2-java-ebean-hikaricp-netty",
    "play2-java-jooq-hikaricp",
    "play2-java-jooq-hikaricp-netty",
    "play2-java-jpa-hikaricp",
    "play2-java-jpa-hikaricp-netty",
    "play2-java-netty",

    "play2-scala",
    "play2-scala-netty",
    "play2-scala-anorm",
    "play2-scala-anorm-netty",
    "play2-scala-reactivemongo",
    "play2-scala-reactivemongo-netty",
    "play2-scala-slick",
    "play2-scala-slick-netty",
]

def main():
    script_dir = os.getenv("FRAMEWORK_DIR")
    os.chdir(script_dir)

    #making log dir
    os.mkdir("run_logs")

    base_command = "./tfb --mode verify --test %s > run_logs/%s.txt"
    for framework in frameworks:
        #making sure prior issues do no affect this test
        os.system("docker system prune -a -f")

        result_log = "verify-%s" % (framework)
        command = base_command % (framework, result_log)
        print(command)
        os.system(command)


if __name__ == "__main__":
    main()
