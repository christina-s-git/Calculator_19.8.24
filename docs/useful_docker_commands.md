# Useful Docker Commands & Exploration Tasks

## Basic Docker Commands

### 1️⃣ Building & Running Containers
- **Build an image**:
  ```sh
  docker build -t flask-calculator .
  ```
- **Run a container**:
  ```sh
  docker run -p 5000:5000 flask-calculator
  ```
- **Run in detached mode**:
  ```sh
  docker run -d -p 5000:5000 flask-calculator
  ```
- **Stop a running container**:
  ```sh
  docker stop <container_id>
  ```

### 2️⃣ Inspecting Containers
- **List running containers**:
  ```sh
  docker ps
  ```
- **List all containers (including stopped ones)**:
  ```sh
  docker ps -a
  ```
- **View container logs**:
  ```sh
  docker logs <container_id>
  ```
- **Inspect a container**:
  ```sh
  docker inspect <container_id>
  ```
- **Enter a running container interactively**:
  ```sh
  docker exec -it <container_id> /bin/sh  # For Alpine-based images
  docker exec -it <container_id> /bin/bash  # For Debian/Ubuntu-based images
  ```

### 3️⃣ Managing Images & Containers
- **List Docker images**:
  ```sh
  docker images
  ```
- **Remove a container**:
  ```sh
  docker rm <container_id>
  ```
- **Remove an image**:
  ```sh
  docker rmi <image_id>
  ```
- **Remove all stopped containers**:
  ```sh
  docker container prune
  ```
- **Remove all unused images**:
  ```sh
  docker image prune -a
  ```

### 4️⃣ Networking & Ports
- **Show container network details**:
  ```sh
  docker network ls
  ```
- **Check port mappings of a running container**:
  ```sh
  docker port <container_id>
  ```

---

## Docker Exploration Tasks 🕵️‍♂️

Use these tasks to practice inspecting and managing your running Flask calculator container.

### 1️⃣ Find the running container's ID
🔎 **Command:**
```sh
docker ps
```
✅ **What to do:** Find the `CONTAINER ID` of your running Flask calculator container.

---

### 2️⃣ Check the container logs
🔎 **Command:**
```sh
docker logs <container_id>
```
✅ **What to do:** View the logs and check for any startup messages.

---

### 3️⃣ Inspect the container’s environment
🔎 **Command:**
```sh
docker inspect <container_id>
```
✅ **What to do:** Find the container’s `IPAddress` and `Mounts`.

---

### 4️⃣ Enter the running container interactively
🔎 **Command:**
```sh
docker exec -it <container_id> /bin/sh
```
✅ **What to do:** Navigate inside the container and check if Python is installed (`python --version`).

---

### 5️⃣ List processes running inside the container
🔎 **Command:**
```sh
docker top <container_id>
```
✅ **What to do:** Check which processes are running inside your container.

---

### 6️⃣ Find the container’s exposed ports
🔎 **Command:**
```sh
docker port <container_id>
```
✅ **What to do:** Identify which ports are mapped between the container and your host machine.

---

### 7️⃣ Run an interactive container session
🔎 **Command:**
```sh
docker run -it flask-calculator /bin/sh
```
✅ **What to do:** Start a new interactive session and manually run Python commands inside the container.

---

### 8️⃣ Stop & Remove the Container
🔎 **Commands:**
```sh
docker stop <container_id>
docker rm <container_id>
```
✅ **What to do:** Stop and remove the container cleanly.

---

These tasks will help you understand how Docker containers work and how to interact with them using CLI commands. 🚀

