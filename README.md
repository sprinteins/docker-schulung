# Docker-Schulung
## Project to dockerize as a practical exercise

### Requirements
- [Python](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop/)
- Postgresql: Local postgresql installation required for sqlalchamy
- Optional for commands:
  - build-essentials For Linux / WSL2:
    ```shell
      apt install build-essential
    ```
    with Sudo:
    ```shell
      sudo apt install build-essential
    ```

### Structure
- [backend](./backend/): The backend is written with FastAPI and working via http
- [database](./database/): A PostgreSQL database starts with pgadmin
- [frontend](./frontend/): The UI is also written with FastAPI and Jinja2 as HTML Template engine

### Commands in root directory
`make` -> Shows all commands (build-essentials required)