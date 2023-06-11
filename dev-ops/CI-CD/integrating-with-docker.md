## Best Practices with Docker

- Before optimization, think how inner loop (code, build, run, test) relates with outer loop (push change, CI build, CI test, deployment).
- Use Docker Hub access token when setting up CI rather than password.
- Reduce build time and number of calls by making use of build cache to reuse layers that have been pulled.
- Have release images go to DockerHub.

```yaml
name: CI to Docker Hub
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Check Out Repo
        uses: actions/checkout@v2

      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}

      - name: Set up Docker Buildx
        id: buildx
        uses: docker/setup-buildx-action@v1

      - name: Build and push
        id: docker_build
        uses: docker/build-push-action@v2
        with:
          context: ./
          file: ./Dockerfile
          push: true
          tags: ${{ secrets.DOCKER_HUB_USERNAME }}/simplewhale:latest

      - name: Image digest
        run: echo ${{ steps.docker_build.outputs.digest }}
```
