## Packages

A package is a directory of .go files. Packages help to organize code into reusable components.

## Modules

A module is a collection of packages with built-in dependencies and versioning. A module comes with two additional files: go.mod and go.sum.

### GOPATH

Go initially delimited a scope for the location of dependencies and custom projects inside a filesystem, which was defined by GOPATH i.e. determines the location of the workspace.

GOPATH could be set to custom paths, and more than one GOPATH could be defined for a single user. However, this was discouraged due to added difficulties in dependency management.

There are three directories under GOPATH:

- src: Holds both the source code of your project and installed dependencies
- pkg: Contains compiled package objects
- bin: Holds binary executables of your applications

```
/home/user/go/         <--- This is your GOPATH
├── bin/
├── pkg/
│   └── linux_amd64/
│       └── github.com/
│           └── someuser/
│               └── somelib.a    <--- Compiled dependency package
└── src/
    ├── github.com/
    │   └── someuser/
    │       └── somelib/         <--- Dependency's source code
    │           └── somelib.go
    └── myapp/                   <--- Your project
        └── main.go
```

Starting form Go 1.11, the modular option became available as an alternative to a workspace defined by GOPATH. This is delimited by go.mod and go.sum files.

When you compile/run the projects, go module will download dependencies repo and cache it in GOPATH/pkg. Similarly, when you install a binary, it installs stuff inside GOPATH/bin or GOBIN if defined. The dependencies are stored in the Go module cache, which are shared across all projects on your system.

```
/home/user/go/        # This is your GOPATH
└── pkg/
    └── mod/
        └── cache/
            └── download/
                └── github.com/
                    └── someuser/
                        └── somelib/     # Source code of the dependency
                            └── somelib.go

```

### go.mod

The go.mod file is the root of dependency management in Go. All the modules which are needed or to be used in the project are maintained in go.mod file.

For all the packages we are going to import/use in our project, it will create an entry of those modules in go.mod. Having a go mod file saves the efforts of running the go get command for each dependent module to run the project successfully.

```sh
$ go mod init
```

### go.sum

The go.sum file verifies dependency integrity.

After running any package building command (go install, go build, go test) for
the first time, it will install all the packages with specific versions i.e which are the latest at that moment.

It will also create a go.sum file which maintains the checksum so when you run the project again it will not install all packages again. But use the cache which is stored inside $GOPATH/pkg/mod directory (module cache directory).

go.sum is a generated file you don’t have to edit or modify this file.

## Commands

### Installing packages

**go install** (with or without a version suffix) is now the **recommended** way to build and install packages in module mode.

In Go 1.18, go get will no longer build packages; it will only be used to add, update, or remove dependencies in go.mod. go get should be used with the -d flag to adjust the current module’s dependencies without building packages, and **use of go get to build and install packages is deprecated**. In a future release, the -d flag will always be enabled.

```sh
$ go install github.com/go-swagger/go-swagger/cmd/swagger
```

### go mod tidy

go mod tidy ensures that the go.mod file matches the source code in the module:

- Adds any missing module requirements necessary to build the current module’s packages and dependencies
- If there are unused dependencies, it will remove those from go.mod accordingly

When we upgrade the version of a specific package in go.mod we need to run the command go mod tidy to update the checksums in go.sum.

```sh
$ go mod tidy
```

### go mod vendor

It generates a vendor directory with the versions available. It copies all third-party dependencies to a vendor folder in your project root.

This will add all the transitive dependencies required in order to run the vendor package.

```sh
$ go mod vendor
```
