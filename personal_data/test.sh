#!/usr/bin/env bash

# Function to check if Docker is installed
check_docker_installed() {
    if ! command -v docker &>/dev/null; then
        echo "Docker could not be found, installing now..."
        install_docker
    else
        echo "Docker is already installed."
    fi
}

# Function to install Docker
install_docker() {
    # Update package info
    sudo apt-get update

    # Install packages to allow apt to use a repository over HTTPS
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release

    # Add Docker’s official GPG key
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    # Set up the stable repository
    echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

    # Install Docker Engine
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
}

# Function to build and run Docker container
build_and_run_container() {
    # Build Docker image
    docker build -t my_mysql .

    # Run Docker container
    docker run --name mysql_instance -p 3333:3333 -d my_mysql
}

# Function to run filtered_logger.py script
run_filtered_logger() {
    # Set Environment Variables
    export PERSONAL_DATA_DB_USERNAME=personal_data_root
    export PERSONAL_DATA_DB_PASSWORD=root_pass
    export PERSONAL_DATA_DB_HOST=localhost
    export PERSONAL_DATA_DB_NAME=personal_data_db
    export PERSONAL_DATA_DB_PORT=3333

    # Run the script
    ./filtered_logger.py
}

# Check if Docker is installed
check_docker_installed

# Build and Run the Docker container
build_and_run_container

# Run the filtered_logger.py script
run_filtered_logger
