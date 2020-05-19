#!/usr/bin/python3

import sys
import os

class Benchmark:
    concurrencyLevels = [16, 32, 64, 128, 256, 512]
    pipelineConcurrencyLevels = [256, 1024, 4096, 16384]
    queryLevels = [1, 5, 10, 15, 20]

    def __init__(self, name, hasConcurrency=False, hasPipelineConcurrency=False, hasQuery=False):
        self.name = name
        self.hasConcurrencyOptions = hasConcurrency
        self.hasPipelineConcurrencyOptions = hasPipelineConcurrency
        self.hasQueryOptions = hasQuery

    def getConcurrencyLevels(self, singleConfig):
        if self.hasConcurrencyOptions:
            return [128] if singleConfig else Benchmark.concurrencyLevels
        else:
            return [None]

    def getPipelineConcurrencyLevels(self, singleConfig):
        if self.hasPipelineConcurrencyOptions:
            return [4096] if singleConfig else Benchmark.pipelineConcurrencyLevels
        else:
            return [None]

    def getQueryLevels(self, singleConfig):
        if self.hasQueryOptions:
            return [10] if singleConfig else Benchmark.queryLevels
        else:
            return [None]



plain = Benchmark("plaintext", hasPipelineConcurrency=True)
json = Benchmark("json", hasConcurrency=True)
query = Benchmark("query", hasQuery=True)
db = Benchmark("db", hasConcurrency=True)
update = Benchmark("update", hasQuery=True)
fortune = Benchmark("fortune", hasConcurrency=True)


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
    "play2-scala-slick-netty",
]

framework_tests = {
    "play2-java": [plain, json],
    "play2-java-netty": [plain, json],
    "play2-scala": [plain, json],
    "play2-scala-netty": [plain, json],
    "play2-java-ebean-hikaricp": [query, db, update, fortune],
    "play2-java-ebean-hikaricp-netty": [query, db, update, fortune],
    "play2-java-jooq-hikaricp": [query, db, update, fortune],
    "play2-java-jooq-hikaricp-netty": [query, db, update, fortune],
    "play2-java-jpa-hikaricp": [query, db, update, fortune],
    "play2-java-jpa-hikaricp-netty": [query, db, update, fortune],
    "play2-scala-anorm": [query, db, update],
    "play2-scala-anorm-netty": [query, db, update],
    "play2-scala-reactivemongo": [query, db, update, fortune],
    "play2-scala-reactivemongo-netty": [query, db, update, fortune],
    "play2-scala-slick-netty": [query, db, fortune],
}

def runBenchmark(framework, benchmark, mode, log_dir=None, run_prefix=None, singleConfig=False, duration=None, cmd="./tfb", addTags=False):
    def genBenchmarkId(concurrency, pipelineConcurrency, query):
        name = "%s_%s_%s" % (framework, benchmark.name, mode)
        if concurrency is not None:
            name += "_concurrency-%d" % (concurrency)
        if pipelineConcurrency is not None:
            name += "_pipelineConcurrency-%d" % (pipelineConcurrency)
        if query is not None:
            name += "_query-%d" % (query)
        return name

    def genTags(concurrency, pipelineConcurrency, query):
        def addArg(args, tag, value):
            args += " %s=%s" % (tag, value)
            return args
        args = ""
        args = addArg(args, "app_framework", framework)
        args = addArg(args, "app_bench", benchmark.name)
        if concurrency is not None:
            args = addArg(args, "concurrency", str(concurrency))
        if pipelineConcurrency is not None:
            args = addArg(args, "pipeline_concurrency", str(pipelineConcurrency))
        if query is not None:
            args = addArg(args, "query", str(query))

        return args

    concurrencyLevels = benchmark.getConcurrencyLevels(singleConfig)
    pipelineConcurrencyLevels = benchmark.getPipelineConcurrencyLevels(singleConfig)
    queryLevels = benchmark.getQueryLevels(singleConfig)

    #ensuring log dir exists
    if log_dir is not None and not os.path.exists(log_dir):
        os.mkdir(log_dir)

    command_prefix = "%s --mode %s --test %s --type %s" \
        % (cmd, mode, framework, benchmark.name)

    if duration is not None:
        command_prefix += " --duration %s" % (duration)

    for concurrency in concurrencyLevels:
        for pipelineConcurrency in pipelineConcurrencyLevels:
            for query in queryLevels:
                command = ""
                if concurrency is not None:
                    command += " --concurrency-levels %d" % (concurrency)
                if pipelineConcurrency is not None:
                    command += " --pipeline-concurrency-levels %d" % (pipelineConcurrency)
                if query is not None:
                    command += " --query-levels %d" % (query)
                benchmarkId = genBenchmarkId(concurrency, pipelineConcurrency, query)
                if run_prefix is not None:
                    run_name = "%s%s" % (run_prefix, benchmarkId)
                    command += " --results-dir %s" % (run_name)
                if addTags:
                    tags = genTags(concurrency, pipelineConcurrency, query)
                    command += " --kamon-args %s" % (tags)
                if log_dir is not None:
                    log = "%s/%s" % (log_dir, benchmarkId)
                    command += " > %s.txt " % (log)
                command = "%s %s" % (command_prefix, command)
                print(command)
                os.system(command)

def main():
    script_dir = os.getenv("FRAMEWORK_DIR")
    os.chdir(script_dir)

    for framework in frameworks:
        tests = framework_tests[framework]
        for test in tests:
            runBenchmark(framework, test, "benchmark", log_dir="run_logs", run_prefix="", cmd="./running_scripts/launch_local.sh",addTags=True, duration="60", singleConfig=True)

if __name__ == "__main__":
    main()
